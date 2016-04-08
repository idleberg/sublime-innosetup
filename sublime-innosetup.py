import sublime
import sublime_plugin
import subprocess
import re

iscc = ''
exists = False
popup_enabled = True
popup_style = ''


class InnoSetup():
  err_lines = {}


def refresh_popup_style(bg_color, text_color):
  global popup_style
  popup_style = (
        '<style>'
        'html {'
        'background-color: ' + bg_color + '; padding: 1px '
        '}'
        'body { margin: 1px; color: ' + text_color + ' } '
        '</style>'
        )


def plugin_loaded():
  global iscc, exists, popup_enabled, popup_style
  try:
    subprocess.call(['iscc'], shell=True)
    iscc = 'iscc'
    exists = True
    settings = sublime.load_settings('Preferences.sublime-settings')
    popup_enabled = settings.get('inno_popup_enabled', True)
    popup_bg = settings.get('inno_popup_bg', '#AAAAAA')
    popup_text = settings.get('inno_popup_text', '#AA4400')
    refresh_popup_style(popup_bg, popup_text)
  except OSError as e:
    print(e)


class LintAction(sublime_plugin.EventListener):
  def on_load_async(self, view):
    self.on_modified_async(view)
  def on_modified_async(self, view):
    if 'Inno' in view.settings().get('syntax'):
      lint(view)
      self.on_selection_modified_async(view)
  def on_selection_modified_async(self, view):
    if 'Inno' not in view.settings().get('syntax'):
      return
    if not popup_enabled:
      return
    file = re.sub('\\\\', '/', view.file_name())
    sel_line = view.rowcol(view.sel()[0].a)[0]
    if sel_line in list(InnoSetup.err_lines[file].keys()):
      html = '<html>' + InnoSetup.err_lines[file][sel_line] + '</html>'
      view.show_popup(popup_style + html, max_width=500)


def lint(view):
  if not exists:
    return
  file = re.sub('\\\\', '/', view.file_name())
  InnoSetup.err_lines[file] = {}
  cmd = [iscc, '/q', '/do', '/O-', file]
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
  out, err = p.communicate()
  if not err:
    return
  line_matcher = re.compile(r'Error on line (\d+).*')
  for msg in err.split('\n'):
    if msg == '' or 'Compile aborted' in msg:
      break
    err_line = int(line_matcher.split(msg)[1]) - 1
    InnoSetup.err_lines[file][err_line] = msg
  highlight(view)


def highlight(view):
  error_regions = []
  file = re.sub('\\\\', '/', view.file_name())
  for item in InnoSetup.err_lines[file]:
    line_region = view.line(view.text_point(item, 0))
    error_regions.append(line_region)
  view.set_status('Inno', 'error in lines:' + str([str(view.rowcol(r.a)[0]+1) + ',' for r in error_regions]))
  view.add_regions('inno_error', error_regions, 'entity.name.type.class.error.inno', 'dot', sublime.DRAW_NO_FILL)


class TogglePopup(sublime_plugin.ApplicationCommand):
  def run(self):
    global popup_enabled
    settings = sublime.load_settings('Preferences.sublime-settings')
    curr = settings.get('inno_popup_enabled', True)
    popup_enabled = not curr
    settings.set('inno_popup_enabled', popup_enabled)


class GotoDefinition(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    symbolname, scope = get_word_and_scope_under_cursor(view)
    if 'support.function.pascal' in scope:
      f, r, c = find_symbol(view, symbolname)
      goto_location(f, r, c)
  def is_enabled(self):
    return 'Inno' in self.view.settings().get('syntax')


class FindUsages(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    current_loc = view.rowcol(view.sel()[0].a)
    sym, scope = get_word_and_scope_under_cursor(view)
    matches = []
    regions = []
    for v in view.window().views():
      if 'Inno' not in v.settings().get('syntax'):
        continue
      file = re.split('(?:.*)\\\\(.*)', v.file_name())[1]
      regs = [file + ' at line ' + str(v.rowcol(r.a)[0] + 1) for r in v.find_all(r'\b' + sym + r'\b')]
      matches += [(v.file_name(), v.rowcol(r.a)) for r in v.find_all(r'\b' + sym + r'\b')]
      regions += regs
    def on_sel(ind):
      if ind == - 1:
        goto_location(view.file_name(), current_loc[0], current_loc[1])
      f, rc = matches[ind]
      goto_location(f, rc[0]+1, rc[1]+1)
    view.window().show_quick_panel(regions, on_sel, sublime.MONOSPACE_FONT, 0, on_sel)
  def is_enabled(self):
    return 'Inno' in self.view.settings().get('syntax')


def find_symbol(view, symbolname):
  for v in view.window().views():
    if 'Inno' not in v.settings().get('syntax'):
      continue
    for sym in v.symbols():
      if symbolname == sym[1]:
        row, col = v.rowcol(sym[0].a)
        return v.file_name(), row+1, col+1
  row, col = view.rowcol(view.sel()[0].a)
  return view.file_name(), row+1, col+1


def get_word_and_scope_under_cursor(view):
    sel_region = view.sel()[0]
    scope = view.scope_name(sel_region.a)
    sym = view.substr(view.word(sel_region.a))
    return sym, scope


def goto_location(filename, row, col):
  window = sublime.active_window()
  window.open_file('%s:%s:%s' % (filename, row, col), sublime.ENCODED_POSITION)
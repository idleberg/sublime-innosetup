import sublime
import sublime_plugin
import subprocess
import re
from shutil import which

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


def load_settings():
  def get_iscc():
    global iscc, exists
    iscc = settings.get('iscc')
    if which(iscc) is None:
      exists = False
      sublime.error_message('ISCC not found!')
    else:
      exists = True
  def get_popup_enabled():
    global popup_enabled
    popup_enabled = settings.get('popup_enabled')
  def get_popup_style():
    popup_text = settings.get('popup_foreground')
    popup_bg = settings.get('popup_background')
    refresh_popup_style(popup_bg, popup_text)
  settings = sublime.load_settings('Inno Setup.sublime-settings')
  get_iscc()
  get_popup_enabled()
  get_popup_style()
  settings.add_on_change('iscc', get_iscc)
  settings.add_on_change('popup_enabled', get_popup_enabled)
  settings.add_on_change('popup_foreground', get_popup_style)
  settings.add_on_change('popup_background', get_popup_style)


def plugin_loaded():
  load_settings()


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
    if file not in InnoSetup.err_lines:
      lint(view)
    sel_line = view.rowcol(view.sel()[0].a)[0]
    if sel_line in InnoSetup.err_lines[file]:
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
  view.set_status('Inno', 'error in lines:' + str([str(view.rowcol(r.a)[0]+1) for r in error_regions]))
  view.add_regions('inno_error', error_regions, 'entity.name.type.class.error.inno', 'dot', sublime.DRAW_NO_FILL)


class GotoDefinition(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    symbolname, scope = get_word_and_scope_under_cursor(view)
    if 'support.function.pascal' in scope:
      d = view.window().lookup_symbol_in_open_files(symbolname)[-1]
      abs_path, row, col = d[0], d[2][0], d[2][1]
      goto_location(abs_path, row, col)
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
      regs = [get_symbol_context(v, r) + ':' + str(v.rowcol(r.a)[0] + 1) + ' in file: ' + file for r in v.find_all(r'\b' + sym + r'\b')]
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


def get_symbol_context(view, region):
  cont = ''
  for s in view.symbols():
    if s[0].a > region.a:
      break
    cont = s[1]
  return cont


def get_word_and_scope_under_cursor(view):
    sel_region = view.sel()[0]
    scope = view.scope_name(sel_region.a)
    sym = view.substr(view.word(sel_region.a))
    return sym, scope


def goto_location(filename, row, col):
  window = sublime.active_window()
  window.open_file('%s:%s:%s' % (filename, row, col), sublime.ENCODED_POSITION)
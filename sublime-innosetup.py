import sublime
import sublime_plugin
import subprocess
import re

iscc = ''
exists = False


def plugin_loaded():
  global iscc, exists
  try:
    subprocess.call(['iscc'], shell=True)
    iscc = 'iscc'
    exists = True
  except OSError as e:
    print(e)

err_lines = {}
style = ('<style>'
         'html {'
         'background-color: #AAAAAA; padding: 1px '
         '}'
         'body { margin: 1px; color: #AA4400 } '
         '</style>')


class LintAction(sublime_plugin.EventListener):
  def on_pre_save_async(self, view):
    if 'Inno' in view.settings().get('syntax'):
      lint(view)
  def on_selection_modified_async(self, view):
    if 'Inno' not in view.settings().get('syntax'):
      return
    sel_line = view.rowcol(view.sel()[0].a)[0]
    print(style)
    if sel_line in list(err_lines.keys()):
      html = '<html>' + err_lines[sel_line] + '</html>'
      view.show_popup(style + html, max_width=500)


def lint(view):
  global err_lines
  err_lines = {}
  if not exists:
    return
  file = re.sub('\\\\', '/', view.file_name())
  cmd = [iscc, '/q', '/do', '/O-', file]
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
  out, err = p.communicate()
  line_matcher = re.compile(r'Error on line (\d+).*')
  for msg in err.split('\n'):
    if msg == '' or 'Compile aborted' in msg:
      break
    err_line = int(line_matcher.split(msg)[1]) - 1
    err_lines[err_line] = msg
  highlight(view, err_lines)


def highlight(view, err_lines):
  error_regions = []
  for item in err_lines:
    line_region = view.line(view.text_point(item, 0))
    error_regions.append(line_region)
  view.add_regions('inno_error', error_regions, 'entity.name.type.class.error.inno', 'dot', sublime.DRAW_NO_FILL)

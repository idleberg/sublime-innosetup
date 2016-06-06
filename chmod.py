# chmod.py (via https://github.com/idleberg/sublime-developer-scripts)

import os, stat, sublime, sublime_plugin

# Array of files, relative to package directory
files = [
    'build.sh'
]

def plugin_loaded():
    from os.path import join
    from package_control import events
    
    # Get name of package folder
    me = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

    if len(files) > 0:
        if (events.install(me) or events.post_upgrade(me)) and os.name is 'posix' or 'mac':
            for file in files:

                # Concat full path
                file_path = join(sublime.packages_path(), me + '/' + file)

                # Change permissions, if file exists
                if os.path.isfile(file_path):
                    sublime.status_message("[%s] chmod +x %s" % (me, file))
                    st = os.stat(file_path)
                    os.chmod(file_path, st.st_mode | stat.S_IEXEC)

    sublime.status_message("[%s] Completed" % me)

# https://gist.github.com/idleberg/03bc3766c760bb4b81e3

import os, stat, sublime, sublime_plugin

# Package name, must match directory name
p = 'Inno Setup'

# Array of files, relative to package directory
files = [
    'build.sh'
]

def plugin_loaded():
    from package_control import events

    if (events.install(p) or events.post_upgrade(p)) and os.name is 'posix' or 'mac':
        for file in files:

            # Concat full path
            f = sublime.packages_path() + '/' + p + '/' + file

            # Change permissions, if file exists
            if os.path.isfile(f):
                st = os.stat(f)
                os.chmod(f, st.st_mode | stat.S_IEXEC)

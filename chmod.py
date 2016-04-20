# https://gist.github.com/idleberg/03bc3766c760bb4b81e3

import os, stat, sublime, sublime_plugin

# Array of files, relative to package directory
files = [
    'build.sh'
]

def plugin_loaded():
    from os.path import join
    from package_control import events

    if (events.install(package) or events.post_upgrade(package)) and os.name is 'posix' or 'mac':
        for file in files:

            # Concat full path
            f = join(sublime.packages_path(), package + '/' + file)

            # Change permissions, if file exists
            if os.path.isfile(f):
                st = os.stat(f)
                os.chmod(f, st.st_mode | stat.S_IEXEC)

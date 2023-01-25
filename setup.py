from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app.py', 
               base=base,
               target_name = 'asistente_inter', 
               icon = "icon.ico"
            )
]

build_options = dict(include_files = ['modules/', 'images/'])

setup(name='app_inter',
      version = '1.0',
      description = 'Assistent Inter App',
      options = {'build_exe': build_options},
      executables = executables)
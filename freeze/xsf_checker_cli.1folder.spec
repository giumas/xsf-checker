# Builds a single-folder EXE for distribution.
# Note that an "unbundled" distribution launches much more quickly, but
# requires an installer program to distribute.
#
# To compile, execute the following within the source directory:
#
# pyinstaller --clean -y freeze/OpenBST.1folder.spec
#
# The resulting .exe file is placed in the dist/Raw folder.
#
# - It may require to manually copy DLL libraries.
# - Uninstall PyQt and sip
# - For QtWebEngine:
#   . copy QtWebEngineProcess.exe in the root
#   . copy in PySide2 both "resources" and "translations" folder
#

from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, TOC
# noinspection PyProtectedMember
from PyInstaller.compat import is_darwin

import sys
sys.modules['FixTk'] = None

from xsf_checker import __version__ as app_version

app_name = "xsf_checker"


def collect_pkg_data(package, include_py_files=False, subdir=None):
    import os
    from PyInstaller.utils.hooks import get_package_paths, remove_prefix, PY_IGNORE_EXTENSIONS

    # Accept only strings as packages.
    if type(package) is not str:
        raise ValueError

    pkg_base, pkg_dir = get_package_paths(package)
    if subdir:
        pkg_dir = os.path.join(pkg_dir, subdir)
    # Walk through all file in the given package, looking for data files.
    data_toc = TOC()
    for dir_path, dir_names, files in os.walk(pkg_dir):

        copy_root_token = os.path.split(dir_path)[-1]
        copy_root = copy_root_token in ["support", "configdata"]
        # if copy_root:
        #     print("- %s" % dir_path)

        for f in files:
            extension = os.path.splitext(f)[1]
            if include_py_files or (extension not in PY_IGNORE_EXTENSIONS):
                source_file = os.path.join(dir_path, f)
                dest_folder = remove_prefix(dir_path, os.path.dirname(pkg_base) + os.sep)
                dest_file = os.path.join(dest_folder, f)
                data_toc.append((dest_file, source_file, 'DATA'))

                if copy_root:
                    source_file = os.path.join(dir_path, f)
                    root_path = os.path.join(os.path.dirname(pkg_base), "hyo2", "grids") + os.sep
                    dest_folder = remove_prefix(dir_path, root_path)
                    dest_file = os.path.join(dest_folder, f)
                    # print("%s -> %s" % (dest_file, source_file))
                    data_toc.append((dest_file, source_file, 'DATA'))

    return data_toc


xsf_checker_data = collect_pkg_data('xsf_checker')
compliance_checker_data = collect_pkg_data('compliance_checker')

if is_darwin:
    icon_file = r'freeze\xsf_checker_cli.icns'
else:
    icon_file = r'freeze\xsf_checker_cli.ico'

a = Analysis(['xsf_checker_cli.py'],
             pathex=[],
             hiddenimports=[
                 "PIL",
                 "scipy.linalg", "scipy._lib.messagestream",
                 "cftime"
             ],
             excludes=[
                 "IPython",
                 "PyQt4", "PyQt5",
                 "sphinx", "sphinx_rtd_theme",
                 "FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter",
                 "wx"
             ],
             hookspath=None,
             runtime_hooks=None)

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='%s.%s' % (app_name, app_version),
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon=icon_file
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               xsf_checker_data,
               compliance_checker_data,
               strip=None,
               upx=True,
               name='%s.%s' % (app_name, app_version)
               )

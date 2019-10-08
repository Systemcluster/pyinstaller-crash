# -*- mode: python -*-

from os import path
from PyInstaller.building.build_main import Analysis, PYZ, EXE

# work-around for https://github.com/pyinstaller/pyinstaller/issues/4064
from distutils import distutils_path  # type: ignore
if distutils_path.endswith('__init__.py'):
    distutils_path = path.dirname(distutils_path)

a = Analysis(
    ['.\\main\__main__.py'],
    pathex=['.\\main'],
    binaries=[],
    datas=[],
    hiddenimports=['distutils'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None,
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True,
    uac_admin=False,
    bootloader_ignore_signals=True,
    icon=False,
)

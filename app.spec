# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['E:\\PythonObject\\CF_USB'],
             binaries=[],
             datas=[('pm3', 'pm3'), ('box64.dll', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Box Drive with CF-USB v1.0.16 MAX',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='logo.ico')

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['BMI_Calculator.py'],
             pathex=['C:\\Users\\NextGen\\Desktop\\Python_File\\BMI'],
             binaries=[],
             datas=[('C:\\Users\\NextGen\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\pyfiglet', './pyfiglet')],
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
          name='BMI_Calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='BMI.ico')

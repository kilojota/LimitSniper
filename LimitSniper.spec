import PyInstaller.config
PyInstaller.config.CONF['distpath'] = 'C:\\Users\\ELDOR\\Documents\\Limit-Sniper'
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['sniper.py'],
             pathex=['C:\\Users\\ELDOR\\Documents\\Limit-Sniper'],
             binaries=[],
             datas=[('abi','abi'),('logs','logs'),('settings.json','settings.json'),('tokens.json','tokens.json'),('transactions.json','transactions.json')],

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
          name='LimitSniperKilo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True) 

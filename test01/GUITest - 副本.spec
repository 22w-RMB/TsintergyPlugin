# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['GUITest.py',
	'D:\\code\\pyhton\\plugin\\test01\\common\\common.py',
	'D:\\code\\pyhton\\plugin\\test01\\common\\excel_helper.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\ah\\ahFileConfig.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\ah\\importData.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\ah\\public_private_date.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\js\\jsFileConfig.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\js\\importData.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\js\\public_private_date.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\mx\\mxFileConfig.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\mx\\importData.py',
	'D:\\code\\pyhton\\plugin\\test01\\provinces\\mx\\public_private_date.py'
	],
    pathex=['D:\\code\\pyhton\\plugin\\test01'],
    binaries=[],
    datas=[('.\\template','template'),('.\\yamlFile','yamlFile')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GUITest',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GUITest',
)

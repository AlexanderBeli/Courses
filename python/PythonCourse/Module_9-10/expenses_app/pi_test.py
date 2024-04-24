import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--windowed',
    '--add-data=ic.png:img'
])
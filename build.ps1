pyinstaller --onefile --uac-admin TimeFormatter.py
cp .\build\TimeFormatter\TimeFormatter.exe.manifest ./
pyinstaller --onefile --uac-admin -r TimeFormatter.exe.manifest,1 TimeFormatter.py

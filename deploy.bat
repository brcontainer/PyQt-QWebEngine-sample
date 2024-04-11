call boot.bat

echo Executing pyinstaller:

pyinstaller --windowed main.py

pause

echo Coping DLLs...

xcopy .env\Lib\site-packages\PyQt5\Qt5\bin\*.dll dist\main /sy

pause

echo Deploy on "./dist/main"

pause

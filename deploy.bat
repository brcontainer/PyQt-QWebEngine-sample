call boot.bat

echo Executando pyinstaller:

pyinstaller --windowed main.py

pause

echo Copiando DLLs extras...

xcopy .env\Lib\site-packages\PyQt5\Qt\bin\*.dll dist\main /sy

pause

cls

echo O deploy esta na pasta "./dist/main"

pause

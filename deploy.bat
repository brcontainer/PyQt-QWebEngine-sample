call boot.bat

echo Executando pyinstaller:

pyinstaller main.py

pause

::for /R .env\Lib\site-packages\PyQt5\Qt\bin %%f in (*.dll) do copy %%f dist\main

echo Copiando DLLs extras...

xcopy .env\Lib\site-packages\PyQt5\Qt\bin\*.dll dist\main /sy

pause

cls

echo O deploy esta na pasta "./dist/main"

pause

echo Executing pyinstaller:
(
    call .env\scripts\activate.bat
) && (
    pyinstaller --windowed main.py
)
echo Deploy on "./dist/main"

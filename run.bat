echo Executing pyinstaller:
call .env\scripts\activate.bat && (
    python main.py
)
echo Deploy on "./dist/main"

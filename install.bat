call .env\scripts\deactivate.bat
(
    python -m venv .env
) && (
    call .env\scripts\activate.bat
) && (
    pip install -r requirements.txt
)

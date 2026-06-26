@echo off
cd /d "%~dp0"

echo Installing dependencies...
pip install playwright requests pyyaml -q

echo Installing Chromium browser...
playwright install chromium

echo.
echo Running script...
python src\runners\main.py

pause

@echo off
REM Quick Start Script for Skool Community Platform
REM This launches a local web server and opens the app in your browser

echo.
echo ================================
echo   Skool Community Platform
echo ================================
echo.
echo Starting local server...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python found! Starting server on http://localhost:8000
    echo.
    echo Press Ctrl+C to stop the server
    echo.
    timeout /t 2
    start http://localhost:8000/index.html
    python -m http.server 8000
) else (
    REM Try Python3
    python3 --version >nul 2>&1
    if %errorlevel% == 0 (
        echo Python3 found! Starting server on http://localhost:8000
        echo.
        echo Press Ctrl+C to stop the server
        echo.
        timeout /t 2
        start http://localhost:8000/index.html
        python3 -m http.server 8000
    ) else (
        REM Try Node.js
        node --version >nul 2>&1
        if %errorlevel% == 0 (
            echo Node.js found! Installing http-server if needed...
            call npx http-server -p 8000
        ) else (
            echo.
            echo ERROR: No suitable server found!
            echo.
            echo Please install one of the following:
            echo   1. Python (https://www.python.org/downloads/)
            echo   2. Node.js (https://nodejs.org/)
            echo.
            echo Or open app.html directly in your browser (double-click it)
            echo.
            pause
        )
    )
)

pause

@echo off

set "TARGET_DIR=C:\Program Files (x86)\IAS\ME ANALYZER PRO"

echo ************************************************************
echo * Granting Full Permissions to Everyone for:
echo * %TARGET_DIR%
echo ************************************************************

if not exist "%TARGET_DIR%" (
    echo ERROR: Directory does not exist: "%TARGET_DIR%"
    echo Please make sure the software is installed correctly.
    pause
    exit /b 1
)

icacls "%TARGET_DIR%" /grant Everyone:(OI)(CI)F /T /Q

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Full permissions have been granted to Everyone.
) else (
    echo.
    echo [ERROR] Failed to apply permissions. 
    echo IMPORTANT: You MUST run this batch file as ADMINISTRATOR.
    echo Right-click the file and select "Run as administrator".
)

echo.
pause

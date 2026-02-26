@echo off
echo ========================================
echo Audio Journal Recorder - FFmpeg Setup
echo ========================================
echo.

REM Check if ffmpeg already exists
if exist "ffmpeg\ffmpeg.exe" (
    echo FFmpeg is already installed!
    echo.
    pause
    exit /b 0
)

echo Downloading FFmpeg (this may take a minute)...
echo.

REM Create ffmpeg directory
if not exist "ffmpeg" mkdir ffmpeg

REM Download ffmpeg using PowerShell
powershell -Command "& { Invoke-WebRequest -Uri 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip' -OutFile 'ffmpeg.zip' }"

if not exist "ffmpeg.zip" (
    echo ERROR: Failed to download FFmpeg
    echo Please download manually from: https://github.com/BtbN/FFmpeg-Builds/releases/latest
    pause
    exit /b 1
)

echo Extracting FFmpeg...
powershell -Command "Expand-Archive -Path 'ffmpeg.zip' -DestinationPath '.' -Force"

REM Copy the binaries
for /d %%d in (ffmpeg-master-*) do (
    copy /Y "%%d\bin\ffmpeg.exe" "ffmpeg\"
    copy /Y "%%d\bin\ffprobe.exe" "ffmpeg\"
    rd /s /q "%%d"
)

REM Clean up
del ffmpeg.zip

if exist "ffmpeg\ffmpeg.exe" (
    echo.
    echo ========================================
    echo FFmpeg installed successfully!
    echo You can now run START-RECORDER.bat
    echo ========================================
) else (
    echo.
    echo ERROR: FFmpeg installation failed
    echo Please try again or download manually
)

echo.
pause

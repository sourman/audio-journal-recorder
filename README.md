# Audio Journal Recorder

A simple Windows audio recording app that auto-starts recording when opened.

## Features

- Auto-starts recording on launch
- Saves to Documents/audio-journal as MP3
- Editable filename
- Select microphone from dropdown
- Real-time audio level visualizer
- Discard & Restart - throw away and start fresh
- Pause/Resume support
- Auto-closes after saving

## Quick Start

### First Time Setup

1. Clone or download this repo
2. Run `setup-ffmpeg.bat` (downloads FFmpeg - one time only)
3. Run `pip install -r requirements.txt`

### To Use

Double-click `START-RECORDER.bat` - recording starts automatically

Or create a desktop shortcut: Right-click `START-RECORDER.bat` → Send to → Desktop

## Controls

| Button | Action |
|--------|--------|
| STOP & SAVE | Stops, saves as MP3, closes app |
| Discard & Restart | Deletes current recording and starts fresh |
| Pause / Resume | Pause or resume recording |

## Audio Level Visualizer

The bars show your input level in real-time:
- Green = Normal speaking level
- Orange = Medium level
- Red = Too loud (may distort)

## File Location

Recordings save to: `C:\Users\YOUR_USERNAME\Documents\audio-journal\`

Example filename: `journal_20260226_143022.mp3`

## Requirements

- Windows 10/11
- Python 3.9 or higher

## Recording Specs

- Format: MP3
- Bitrate: 128 kbps
- Sample Rate: 44.1 kHz
- Channels: Mono

## Troubleshooting

**No audio recording?**
- Check your microphone is selected in the dropdown
- Verify Windows microphone privacy settings

**FFmpeg errors?**
- Run `setup-ffmpeg.bat` again
- Make sure `ffmpeg/ffmpeg.exe` exists in the app folder

## License

MIT License

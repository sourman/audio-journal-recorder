# Captain's Log

An audio journal recorder for Windows. Engage recording with one click.

## Mission Parameters

- Auto-starts recording on launch (Engage!)
- Saves to Documents/audio-journal as MP3
- Editable filename (name your log entry)
- Select microphone from dropdown (choose your channel)
- Real-time audio level visualizer
- Discard & Restart - try again, no red shirts harmed
- Pause/Resume support
- Auto-closes after saving (Mission complete)

## Quick Start

### First Time Setup

1. Clone or download this repo
2. Run `setup-ffmpeg.bat` (downloads the main deflector - one time only)
3. Run `pip install -r requirements.txt`

### To Use

Double-click `START-RECORDER.bat` - recording starts automatically

Or create a desktop shortcut: Right-click `START-RECORDER.bat` → Send to → Desktop

## Bridge Controls

| Button | Action |
|--------|--------|
| STOP & SAVE | Saves log entry and closes channel |
| Discard & Restart | Timeline reset - try that again |
| Pause / Resume | Hold position |

## Audio Level Visualizer

The bars show your input level in real-time:
- Green = Optimal transmission level
- Orange = Raising shields (getting loud)
- Red = Warp core overload (too loud!)

## Log Storage

All logs saved to: `C:\Users\YOUR_USERNAME\Documents\audio-journal\`

Example filename: `journal_20260226_143022.mp3`

## Technical Specifications

- Format: MP3
- Bitrate: 128 kbps
- Sample Rate: 44.1 kHz
- Channels: Mono

## Requirements

- Windows 10/11
- Python 3.9 or higher

## Troubleshooting

**No audio recording?**
- Check your microphone selection (comms channel)
- Verify Windows microphone privacy settings

**FFmpeg errors?**
- Run `setup-ffmpeg.bat` again
- Make sure `ffmpeg/ffmpeg.exe` exists in the app folder

## License

MIT License - Make it so.

---

*Live long and record.*

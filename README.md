# 🎙️ Audio Journal Recorder

A super simple Windows audio recording app that auto-starts recording when opened. Perfect for quick voice memos, journal entries, or audio notes.

![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![Windows](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- ✅ **Auto-starts recording** on launch (one-click!)
- ✅ **Saves as MP3** to `Documents/audio-journal`
- ✅ **Editable filename** before/during recording
- ✅ **Select microphone** from dropdown (multi-mic support)
- ✅ **Real-time audio visualizer** - see your voice levels
- ✅ **Discard & Restart** - throw away and start fresh instantly
- ✅ **Pause/Resume** support
- ✅ **Auto-closes** after saving

## 🎬 Quick Start

### First Time Setup

1. Clone or download this repo
2. **Run `setup-ffmpeg.bat`** (downloads FFmpeg - one time only)
3. Run `pip install -r requirements.txt` (install Python dependencies)

### Option 1: Desktop Shortcut (Recommended)

1. Right-click `START-RECORDER.bat`
2. Send to → Desktop (create shortcut)
3. Double-click the shortcut to start recording!

### Option 2: From Folder

1. Double-click `START-RECORDER.bat`
2. Recording starts automatically

## 📋 How to Use

1. **Launch the app** - Recording starts automatically
2. **Select your microphone** (if you have multiple)
3. **Edit the filename** if you want a custom name
4. **Watch the visualizer** to confirm audio is being captured
5. **Click "STOP & SAVE"** when done - app closes automatically
   - OR click **"🔄 Discard & Restart"** to throw away and start fresh

## 🎚️ Controls

| Button | Action |
|--------|--------|
| ⏹️ **STOP & SAVE** | Stops recording, saves as MP3, closes app |
| 🔄 **Discard & Restart** | Deletes current recording and starts fresh instantly |
| ⏸️ **Pause / ▶️ Resume** | Pause or resume recording |

## 📊 Audio Level Visualizer

The bars show your input level in real-time:
- 🟢 **Green** = Normal speaking level ✅
- 🟠 **Orange** = Medium level
- 🔴 **Red** = Too loud (may distort) ⚠️

**Tip**: Speak at a normal distance from your mic. Aim for green/orange bars, avoid constant red.

## 📁 File Locations

**Recordings saved to:**
```
C:\Users\YOUR_USERNAME\Documents\audio-journal\
```

**Example filename:** `journal_20260226_143022.mp3`

## 🛠️ Setup (First Time Only)

### Prerequisites

- Windows 10/11
- Python 3.9 or higher

### Install

1. **Download FFmpeg** - Double-click `setup-ffmpeg.bat` (one-time setup)
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

That's it! You're ready to record.

## 📦 What's Included

```
audio-journal-recorder/
├── audio-journal-recorder.py   # Main application
├── START-RECORDER.bat          # One-click launcher
├── setup-ffmpeg.bat            # Downloads FFmpeg (run once)
├── requirements.txt            # Python dependencies
├── ffmpeg/                     # FFmpeg binaries (created by setup script)
│   ├── ffmpeg.exe
│   └── ffprobe.exe
└── README.md                   # This file
```

## 🎯 Recording Specs

- **Format:** MP3
- **Bitrate:** 128 kbps
- **Sample Rate:** 44.1 kHz
- **Channels:** Mono (voice optimized)

## 💡 Use Cases

- 📔 **Audio Journaling** - Daily thoughts and reflections
- 🎤 **Voice Memos** - Quick notes to self
- 📚 **Lecture Recording** - Capture classes or meetings
- 🎵 **Voice Practice** - Singing or speech practice
- 💬 **Voice Messages** - Record audio for messages

## 🔄 Discard & Restart Feature

The **"Discard & Restart"** button is perfect when:
- You messed up the beginning → Start fresh instantly
- You want to re-record → Delete and try again
- You changed your mind → New topic, new recording

The audio stream never stops - it just resets the buffer and continues recording from that exact moment!

## 🐛 Troubleshooting

**No audio recording?**
- Check your microphone is selected in the dropdown
- Verify Windows microphone privacy settings
- Check your system microphone isn't muted

**FFmpeg errors?**
- The app falls back to WAV format if MP3 conversion fails
- Make sure `ffmpeg/ffmpeg.exe` exists in the app folder

**Can't hear playback?**
- Check the file in `Documents/audio-journal/`
- Try playing with VLC or Windows Media Player

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Feel free to submit issues or pull requests!

---

**Made with ❤️ for quick and easy audio recording**

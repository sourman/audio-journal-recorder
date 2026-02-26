# Audio Journal Recorder

A super simple Windows audio recording app that auto-starts recording when opened.

## Features
- ✅ Auto-starts recording on launch (one-click!)
- ✅ Saves automatically to `Documents/audio-journal` as MP3
- ✅ **Editable filename** before/during recording
- ✅ **Select microphone** from dropdown
- ✅ **Audio level visualizer** - see your voice in real-time
- ✅ **Discard & Restart** - throw away and start fresh instantly
- ✅ Pause/Resume support
- ✅ **Auto-closes** after saving

## UI Layout

```
┌─────────────────────────────────────┐
│     🎙️ Audio Journal Recorder       │
│                                     │
│  🎤 Microphone: [Select Device ▼]   │
│  📝 Filename: [journal_2026...] .mp3│
│                                     │
│     Status: 🔴 Recording...         │
│                                     │
│          00:00                      │
│                                     │
│     Audio Level:                    │
│  ┌─────────────────────────────┐    │
│  │ ▅▆▄█▇▃▆▅▄▂█▆▅▄▂█▇▅▄▃▂█    │    │
│  └─────────────────────────────┘    │
│                                     │
│   ┌─────────────────────────────┐   │
│   │     ⏹️ STOP & SAVE          │   │
│   └─────────────────────────────┘   │
│   ┌───────────────────────────────┐ │
│   │   🔄 Discard & Restart        │ │
│   └───────────────────────────────┘ │
│   ┌───────────────────────────┐     │
│   │       ⏸️ Pause             │     │
│   └───────────────────────────┘     │
│                                     │
│  💾 Saved to: Documents/audio-journal│
└─────────────────────────────────────┘
```

## How to Use

1. **Double-click `START-RECORDER.bat`**
2. **Select your microphone** (if you have multiple)
3. **Edit the filename** if you want a custom name
4. **Recording starts automatically** after 0.5 seconds
5. **Watch the visualizer** to confirm audio is being captured
6. **Click "STOP & SAVE"** when done - app closes automatically
   - OR click **"🔄 Discard & Restart"** to throw away and start fresh instantly

## Audio Level Visualizer

The bars show your input level in real-time:
- 🟢 **Green** = Normal level
- 🟠 **Orange** = Medium level
- 🔴 **Red** = High level (may distort)

**Tip**: Speak at a normal distance from your mic. Aim for green/orange bars, avoid constant red.

## Controls

| Button | Action |
|--------|--------|
| ⏹️ STOP & SAVE | Stops recording, saves as MP3, closes app |
| 🔄 Discard & Restart | Deletes current recording and starts fresh instantly |
| ⏸️ Pause / ▶️ Resume | Pause or resume recording |

## Where Recordings Are Saved

All recordings go to: `C:\Users\USER\Documents\audio-journal\`

Example filename: `journal_20260226_143022.mp3` (or your custom name)

## Setup (First Time Only)

If you haven't installed dependencies yet:

```powershell
cd C:\Users\USER\workspace\captain-log
pip install -r requirements.txt
```

## Creating a Desktop Shortcut

1. Right-click `START-RECORDER.bat`
2. Send to → Desktop (create shortcut)

Now you can record with one double-click from your desktop!

## Notes

- Recording format: MP3 (128kbps, 44.1kHz, mono)
- Uses your selected microphone (or system default)
- Recording starts automatically 0.5 seconds after opening
- App closes automatically 1 second after saving

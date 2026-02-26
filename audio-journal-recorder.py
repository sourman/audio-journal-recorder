#!/usr/bin/env python3
"""
Simple Audio Journal Recorder
Auto-starts recording on launch and saves to Documents/audio-journal as MP3
"""

import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import numpy as np
import os
import subprocess
import wave
from datetime import datetime

class AudioJournalRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio Journal Recorder")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        # Setup ffmpeg path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(script_dir, "ffmpeg", "ffmpeg.exe")

        # Recording state
        self.is_recording = False
        self.is_paused = False
        self.recording_data = []
        self.start_time = None
        self.stream = None
        self.audio_level = 0
        self.level_history = [0] * 50

        # Setup output directory
        self.output_dir = os.path.join(os.path.expanduser("~"), "Documents", "audio-journal")
        os.makedirs(self.output_dir, exist_ok=True)

        # Get available audio devices
        self.devices = self.get_audio_devices()
        self.selected_device = tk.StringVar()
        if self.devices:
            self.selected_device.set(self.devices[0])

        # Build UI
        self._build_ui()

        # Auto-start recording
        self.root.after(500, self.start_recording)

        # Start visualizer update
        self.update_visualizer()

    def get_audio_devices(self):
        """Get list of audio input devices"""
        try:
            devices = sd.query_devices()
            input_devices = []
            for i, device in enumerate(devices):
                if device['max_input_channels'] > 0:
                    input_devices.append(f"{i}: {device['name']}")
            return input_devices if input_devices else ["Default"]
        except Exception as e:
            print(f"Error getting devices: {e}")
            return ["Default"]

    def _build_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="🎙️ Audio Journal Recorder",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 10))

        # Device selection
        device_frame = ttk.Frame(main_frame)
        device_frame.pack(fill=tk.X, pady=5)

        ttk.Label(
            device_frame,
            text="🎤 Microphone:",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 10))

        if len(self.devices) > 1:
            self.device_dropdown = ttk.Combobox(
                device_frame,
                textvariable=self.selected_device,
                values=self.devices,
                state="readonly",
                width=35
            )
            self.device_dropdown.pack(side=tk.LEFT)
        else:
            ttk.Label(
                device_frame,
                text=self.devices[0] if self.devices else "Default",
                font=("Arial", 9)
            ).pack(side=tk.LEFT)

        # Filename entry
        filename_frame = ttk.Frame(main_frame)
        filename_frame.pack(fill=tk.X, pady=10)

        ttk.Label(
            filename_frame,
            text="📝 Filename:",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 10))

        # Generate default filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename_var = tk.StringVar(value=f"journal_{timestamp}")
        self.filename_entry = ttk.Entry(
            filename_frame,
            textvariable=self.filename_var,
            width=30,
            font=("Consolas", 10)
        )
        self.filename_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(filename_frame, text=".mp3").pack(side=tk.LEFT)

        # Status
        self.status_label = ttk.Label(
            main_frame,
            text="Status: Initializing...",
            font=("Arial", 11, "bold")
        )
        self.status_label.pack(pady=8)

        # Timer
        self.timer_label = ttk.Label(
            main_frame,
            text="00:00",
            font=("Consolas", 36, "bold"),
            foreground="#333"
        )
        self.timer_label.pack(pady=10)

        # Audio Level Visualizer
        visualizer_frame = ttk.Frame(main_frame)
        visualizer_frame.pack(pady=10, fill=tk.X)

        ttk.Label(
            visualizer_frame,
            text="Audio Level:",
            font=("Arial", 9)
        ).pack()

        self.canvas = tk.Canvas(
            visualizer_frame,
            width=400,
            height=80,
            bg="#1a1a1a",
            highlightthickness=1,
            highlightbackground="#444"
        )
        self.canvas.pack(pady=5)

        # Buttons container
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=15)

        # Stop button - BIG and prominent
        self.stop_button = tk.Button(
            buttons_frame,
            text="⏹️ STOP & SAVE",
            command=self.stop_recording,
            font=("Arial", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            width=20,
            height=2,
            relief=tk.RAISED,
            bd=3
        )
        self.stop_button.pack(pady=8)

        # Restart/Discard button
        self.restart_button = tk.Button(
            buttons_frame,
            text="🔄 Discard & Restart",
            command=self.restart_recording,
            font=("Arial", 11),
            bg="#8e44ad",
            fg="white",
            activebackground="#71368a",
            activeforeground="white",
            width=18,
            height=1,
            state=tk.DISABLED,
            relief=tk.RAISED,
            bd=2
        )
        self.restart_button.pack(pady=5)

        # Pause/Resume button
        self.pause_button = tk.Button(
            buttons_frame,
            text="⏸️ Pause",
            command=self.toggle_pause,
            font=("Arial", 11),
            bg="#f39c12",
            fg="white",
            activebackground="#d68910",
            activeforeground="white",
            width=15,
            height=1,
            state=tk.DISABLED,
            relief=tk.RAISED,
            bd=2
        )
        self.pause_button.pack(pady=5)

        # Footer info
        info_label = ttk.Label(
            main_frame,
            text="💾 Saved to: Documents/audio-journal",
            font=("Arial", 9),
            foreground="#888"
        )
        info_label.pack(side=tk.BOTTOM, pady=10)

    def update_visualizer(self):
        """Update the audio level visualizer"""
        # Update history with current level
        self.level_history.pop(0)
        self.level_history.append(self.audio_level)

        # Clear canvas
        self.canvas.delete("all")

        # Draw bars
        bar_width = 400 // len(self.level_history)
        for i, level in enumerate(self.level_history):
            x1 = i * bar_width
            x2 = x1 + bar_width - 1

            # Color based on level
            if level > 0.7:
                color = "#e74c3c"  # Red for high levels
            elif level > 0.4:
                color = "#f39c12"  # Orange for medium
            else:
                color = "#27ae60"  # Green for normal

            # Height based on level (min 5px so we can see it's recording)
            height = max(5, int(level * 70))
            y1 = 40 - height // 2
            y2 = 40 + height // 2

            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color,
                outline=""
            )

        # Draw center line
        self.canvas.create_line(0, 40, 400, 40, fill="#333", width=1)

        # Decay level
        self.audio_level = max(0, self.audio_level - 0.05)

        # Schedule next update
        self.root.after(50, self.update_visualizer)

    def update_timer(self):
        if self.is_recording and not self.is_paused:
            elapsed = datetime.now() - self.start_time
            minutes, seconds = divmod(int(elapsed.total_seconds()), 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)

    def get_device_index(self):
        """Extract device index from selected device string"""
        try:
            device_str = self.selected_device.get()
            if device_str and ":" in device_str:
                return int(device_str.split(":")[0])
        except:
            pass
        return None  # Use default device

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(f"Audio callback status: {status}")

        if not self.is_paused and self.is_recording:
            # Store audio data
            self.recording_data.append(indata.copy())

            # Calculate audio level for visualization
            rms = np.sqrt(np.mean(indata ** 2))
            self.audio_level = max(self.audio_level, min(1.0, rms * 5))

    def start_recording(self):
        if self.is_recording:
            return

        try:
            self.is_recording = True
            self.is_paused = False
            self.recording_data = []
            self.start_time = datetime.now()

            # Get filename from entry
            base_name = self.filename_var.get().strip()
            if not base_name:
                base_name = f"journal_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            if not base_name.endswith('.mp3'):
                base_name += '.mp3'
            self.current_filename = base_name
            self.current_filepath = os.path.join(self.output_dir, self.current_filename)

            # Get device index
            device_index = self.get_device_index()

            # Update UI
            self.status_label.config(text="🔴 Recording...", foreground="#e74c3c")
            self.stop_button.config(state=tk.NORMAL, bg="#e74c3c")
            self.restart_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.filename_entry.config(state=tk.DISABLED)

            # Disable device dropdown during recording
            if hasattr(self, 'device_dropdown'):
                self.device_dropdown.config(state=tk.DISABLED)

            # Start audio stream
            stream_args = {
                'samplerate': 44100,
                'channels': 1,
                'dtype': np.float32,
                'callback': self.audio_callback
            }
            if device_index is not None:
                stream_args['device'] = device_index

            self.stream = sd.InputStream(**stream_args)
            self.stream.start()

            # Start timer
            self.update_timer()

        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)}", foreground="red")
            print(f"Error starting recording: {e}")

    def stop_recording(self):
        if not self.is_recording:
            return

        try:
            self.is_recording = False
            self.status_label.config(text="💾 Saving...", foreground="#f39c12")
            self.root.update()

            # Stop stream
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None

            # Save recording as MP3
            if self.recording_data:
                # Concatenate all audio chunks
                audio_data = np.concatenate(self.recording_data, axis=0)

                # Convert to int16
                audio_data = (audio_data * 32767).astype(np.int16)

                # Create temporary WAV file
                temp_wav = self.current_filepath.replace('.mp3', '_temp.wav')

                # Write WAV file
                with wave.open(temp_wav, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(44100)
                    wf.writeframes(audio_data.tobytes())

                # Convert WAV to MP3 using ffmpeg
                try:
                    result = subprocess.run(
                        [self.ffmpeg_path, '-i', temp_wav, '-b:a', '128k', self.current_filepath, '-y'],
                        check=True,
                        capture_output=True
                    )
                    # Remove temporary WAV file
                    os.remove(temp_wav)

                    # Show success briefly
                    self.status_label.config(
                        text=f"✅ Saved: {self.current_filename}",
                        foreground="#27ae60"
                    )
                    self.root.update()

                    # Close app after a brief moment
                    self.root.after(1000, self.root.destroy)

                except subprocess.CalledProcessError as e:
                    # If ffmpeg fails, keep the WAV file
                    print(f"FFmpeg error: {e}")
                    wav_path = self.current_filepath.replace('.mp3', '.wav')
                    os.rename(temp_wav, wav_path)
                    self.current_filename = os.path.basename(wav_path)

                    self.status_label.config(
                        text=f"✅ Saved: {self.current_filename}",
                        foreground="#27ae60"
                    )
                    self.root.update()

                    # Close app after a brief moment
                    self.root.after(1000, self.root.destroy)

        except Exception as e:
            self.status_label.config(text=f"❌ Save Error: {str(e)}", foreground="red")
            print(f"Error saving recording: {e}")
            self.root.update()
            # Still close after showing error
            self.root.after(2000, self.root.destroy)

    def restart_recording(self):
        """Discard current recording and start fresh without stopping the stream"""
        if not self.is_recording:
            return

        try:
            # Show feedback
            self.status_label.config(text="🔄 Discarded & Restarting...", foreground="#8e44ad")
            self.root.update()

            # Clear the recording data
            self.recording_data = []

            # Reset the timer
            self.start_time = datetime.now()
            self.timer_label.config(text="00:00")

            # Update filename to new timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_base_name = f"journal_{timestamp}"
            self.filename_var.set(new_base_name)
            self.current_filename = new_base_name + ".mp3"
            self.current_filepath = os.path.join(self.output_dir, self.current_filename)

            # Resume if paused
            if self.is_paused:
                self.is_paused = False
                self.pause_button.config(text="⏸️ Pause")

            # Brief delay then show recording status again
            self.root.after(500, lambda: self.status_label.config(
                text="🔴 Recording...",
                foreground="#e74c3c"
            ))

        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)}", foreground="red")
            print(f"Error restarting recording: {e}")

    def toggle_pause(self):
        if not self.is_recording:
            return

        self.is_paused = not self.is_paused

        if self.is_paused:
            self.status_label.config(text="⏸️ Paused", foreground="#f39c12")
            self.pause_button.config(text="▶️ Resume")
        else:
            self.status_label.config(text="🔴 Recording...", foreground="#e74c3c")
            self.pause_button.config(text="⏸️ Pause")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AudioJournalRecorder()
    app.run()

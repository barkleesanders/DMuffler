"""
__author__     = ["Blaze Sanders"]
__email__      = ["dev@blazesanders.com"]
__license__    = "MIT"
__status__     = "Development"
__deprecated__ = "False"
__version__    = "0.0.1"
__doc__        = "Create pitch varying audio in real-time on low processing power CPUs"
"""


## Standard Python libraries
import time            # https://docs.python.org/3/library/time.html
import threading       # https://docs.python.org/3/library/threading.html

## 3rd party libraries
try:
    # Peek makes printing debug information easy and adds basic benchmarking functionality (see https://salabim.org/peek)
    # pip install peek-python
    from peek import peek  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    def peek(message: str, **_kwargs) -> None:
        """Fallback debug printer when :mod:`peek` is unavailable."""
        print(message)

try:
    # Audio analysis, with building blocks necessary to create music information retrieval systems
    # https://librosa.org/doc/latest/index.html
    import librosa

    # Play and record NumPy arrays containing audio signals.
    # https://python-sounddevice.readthedocs.io/
    import sounddevice as sd
    import numpy as np

    # Control and monitor input devices (mouse & keyboard)
    # https://pypi.org/project/pynput/
    from pynput import keyboard

except ModuleNotFoundError as exc:  # pragma: no cover - runtime guard
    peek("Please verify that .venvDMuffler virtual environment is running", color="red")
    peek("source .venvDMuffler/bin/activate", color="yellow")
    peek("pip install -r requirements.txt", color="yellow")
    peek(f"Missing dependency: {exc}", color="red")
    librosa = None
    sd = None
    np = None
    keyboard = None

class EngineSoundPitchShifter:

    def __init__(self):
        """Initialize playback state."""
        self.playing = False
        self.pitch_factor = 1.0
        self.current_frame = 0
        self.running = True

    def on_press(self, key):
        try:
            # Space bar controls playback
            if key == keyboard.Key.space:
                self.playing = not self.playing
                print(f"Playback: {'Playing' if self.playing else 'Paused'}")

            # Up arrow increases pitch
            elif key == keyboard.Key.up:
                self.pitch_factor = min(2.0, self.pitch_factor + 0.1)
                print(f"Pitch factor: {self.pitch_factor:.1f}")

            # Down arrow decreases pitch
            elif key == keyboard.Key.down:
                self.pitch_factor = max(0.5, self.pitch_factor - 0.1)
                print(f"Pitch factor: {self.pitch_factor:.1f}")

            # R key resets playback
            elif hasattr(key, 'char') and key.char == 'r':
                self.current_frame = 0
                print("Playback reset")

            # ESC key exits
            elif key == keyboard.Key.esc:
                self.running = False
                return False

        except AttributeError:
            pass

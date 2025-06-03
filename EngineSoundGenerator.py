#!/usr/bin/env python3
"""Engine sound generation utilities."""

import logging

try:
    import simpleaudio as sa
except ModuleNotFoundError:  # pragma: no cover - runtime guard
    sa = None


class EngineSoundGenerator:
    """Load and play sample engine sounds."""

    MC_LAREN_F1 = "McLarenF1.wav"
    LA_FERRARI = "LaFerrari.wav"
    PORCSHE_911 = "Porcshe911.wav"
    BMW_M4 = "BMW_M4.wav"
    JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.wav"
    FORD_MODEL_T = "FordModelT.wav"
    FORD_MUSTANG_GT350 = "FordMustangGT350.wav"

    def __init__(self, base_audio):
        self.log = logging.getLogger(__name__)
        self.EngineSoundsDict = {
            self.MC_LAREN_F1: 0,
            self.LA_FERRARI: 1,
            self.PORCSHE_911: 2,
            self.BMW_M4: 3,
            self.JAGUAR_E_TYPE_SERIES_1: 4,
            self.FORD_MODEL_T: 5,
            self.FORD_MUSTANG_GT350: 6,
        }

        if isinstance(base_audio, str) and base_audio in self.EngineSoundsDict:
            self.baseAudioFilename = base_audio
            self.engineSoundID = self.EngineSoundsDict[base_audio]
        else:
            self.log.info(
                "Invalid engine sound '%s', defaulting to McLaren F1", base_audio
            )
            self.baseAudioFilename = self.MC_LAREN_F1
            self.engineSoundID = self.EngineSoundsDict[self.MC_LAREN_F1]

        if sa:
            path = "./Sounds/" + self.baseAudioFilename
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(path)
        else:  # pragma: no cover - runtime guard
            self.EngineSoundWaveObject = None

    def startAudio(self):
        """Play the engine sound once."""
        if not self.EngineSoundWaveObject:
            raise RuntimeError("simpleaudio not available")
        return self.EngineSoundWaveObject.play()

    @staticmethod
    def stopAudio(play_obj):
        """Stop playback returned by :meth:`startAudio`."""
        play_obj.stop()

    def get_base_audio_filename(self):
        """Return the file name currently configured."""
        return self.baseAudioFilename

    def get_engine_sound_id(self):
        """Return the numeric ID of the current sound."""
        return self.engineSoundID


__all__ = ["EngineSoundGenerator"]

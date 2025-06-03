#!/usr/bin/env python3
"""
EngineSoundGenerator
--------------------
Simple utility class used in DMuffler to play engine sounds. The original file
contained unresolved merge conflicts. This version keeps a minimal feature set so
the module can be imported and unit tested without the audio library installed.
"""

import logging

try:
    import simpleaudio as sa
except ModuleNotFoundError:
    sa = None
    print("simpleaudio not installed - audio playback disabled")


class EngineSoundGenerator:
    """Utility to load and play engine sounds."""

    MC_LAREN_F1 = "McLarenF1.wav"
    LA_FERRARI = "LaFerrari.wav"
    PORCSHE_911 = "Porcshe911.wav"
    BMW_M4 = "BMW_M4.wav"
    JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.wav"
    FORD_MODEL_T = "FordModelT.wav"
    FORD_MUSTANG_GT350 = "FordMustangGT350.wav"

    def __init__(self, baseAudio):
        self.log = logging.getLogger(__name__)
        self.EngineSoundsDict = {
            EngineSoundGenerator.MC_LAREN_F1: 0,
            EngineSoundGenerator.LA_FERRARI: 1,
            EngineSoundGenerator.PORCSHE_911: 2,
            EngineSoundGenerator.BMW_M4: 3,
            EngineSoundGenerator.JAGUAR_E_TYPE_SERIES_1: 4,
            EngineSoundGenerator.FORD_MODEL_T: 5,
            EngineSoundGenerator.FORD_MUSTANG_GT350: 6,
        }

        if baseAudio not in self.EngineSoundsDict:
            self.log.info(
                "Invalid engine sound, defaulting to McLaren F1")
            baseAudio = EngineSoundGenerator.MC_LAREN_F1

        self.engineSoundID = self.EngineSoundsDict[baseAudio]
        self.baseAudioFilename = baseAudio
        path = "./Sounds/" + baseAudio
        if sa is not None:
            try:
                self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(path)
            except Exception as exc:
                self.log.error("Failed to load sound %s: %s", path, exc)
                self.EngineSoundWaveObject = None
        else:
            self.EngineSoundWaveObject = None

    def startAudioLoop(self):
        """Play sound continuously until finished."""
        if self.EngineSoundWaveObject is None:
            self.log.warning("Audio playback not available")
            return
        playObj = self.EngineSoundWaveObject.play()
        playObj.wait_done()

    def startAudio(self):
        """Play sound once and return the playback object."""
        if self.EngineSoundWaveObject is None:
            self.log.warning("Audio playback not available")
            return None
        return self.EngineSoundWaveObject.play()

    def stopAudio(self, playObj):
        """Stop previously started playback."""
        if playObj is not None:
            playObj.stop()

    def setNewSound(self, newSound):
        """Change the loaded engine sound."""
        if newSound not in self.EngineSoundsDict:
            self.log.warning("New sound was NOT set. Keeping current sound")
            return
        self.engineSoundID = self.EngineSoundsDict[newSound]
        self.baseAudioFilename = newSound
        path = "./Sounds/" + newSound
        if sa is not None:
            try:
                self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(path)
            except Exception as exc:
                self.log.error("Failed to load sound %s: %s", path, exc)
                self.EngineSoundWaveObject = None
        else:
            self.EngineSoundWaveObject = None

    def getBaseAudio(self):
        return self.baseAudioFilename

    def getbaseAudioFilename(self):
        return int(self.engineSoundID)

    @staticmethod
    def unitTest():
        print("STARTING EngineSoundGenerator.py Unit Test")
        obj = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        assert obj.getbaseAudioFilename() == obj.EngineSoundsDict[EngineSoundGenerator.MC_LAREN_F1]
        playObj = obj.startAudio()
        obj.stopAudio(playObj)
        print("EngineSoundGenerator.py Unit Test COMPLETE")


if __name__ == "__main__":
    EngineSoundGenerator.unitTest()

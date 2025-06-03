import unittest
from unittest.mock import MagicMock, patch

from EngineSoundGenerator import EngineSoundGenerator


class EngineSoundGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.wave_obj = MagicMock()
        self.play_obj = MagicMock()
        self.wave_obj.play.return_value = self.play_obj

    @patch('EngineSoundGenerator.sa')
    def test_valid_sound_selection(self, mock_sa):
        mock_sa.WaveObject.from_wave_file.return_value = self.wave_obj

        gen = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        self.assertEqual(
            gen.get_base_audio_filename(), EngineSoundGenerator.MC_LAREN_F1
        )
        self.assertEqual(
            gen.get_engine_sound_id(),
            gen.EngineSoundsDict[EngineSoundGenerator.MC_LAREN_F1],
        )

        returned = gen.startAudio()
        self.assertIs(returned, self.play_obj)
        self.wave_obj.play.assert_called_once()

        EngineSoundGenerator.stopAudio(returned)
        self.play_obj.stop.assert_called_once()

    @patch('EngineSoundGenerator.sa')
    def test_invalid_sound_defaults_to_mclaren(self, mock_sa):
        mock_sa.WaveObject.from_wave_file.return_value = self.wave_obj

        gen = EngineSoundGenerator(10)
        self.assertEqual(
            gen.get_base_audio_filename(), EngineSoundGenerator.MC_LAREN_F1
        )
        self.assertEqual(
            gen.get_engine_sound_id(),
            gen.EngineSoundsDict[EngineSoundGenerator.MC_LAREN_F1],
        )
        mock_sa.WaveObject.from_wave_file.assert_called_with(
            "./Sounds/" + EngineSoundGenerator.MC_LAREN_F1
        )


if __name__ == '__main__':
    unittest.main()

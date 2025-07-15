"""
Unit tests for IX-ThermaForge beam modulation modules.
Author: Bryce Wooster
Date: 2025-07-15
"""

import unittest
import time
from src.controller_firmware.main_controller import HarmonicController

class TestHarmonicController(unittest.TestCase):
    def setUp(self):
        self.controller = HarmonicController(base_frequency_hz=60.0)

    def test_frequency_cycle(self):
        freqs = []
        # Collect frequencies over 6 seconds to cover two full cycles
        for i in range(6):
            freq = self.controller.get_next_pattern_frequency()
            freqs.append(freq)
            time.sleep(1)
        expected_sequence = [180, 360, 540] * 2  # 60*3, 60*6, 60*9 repeated twice
        self.assertEqual(freqs, expected_sequence)

    def test_modulate_beam_pattern_output(self):
        output = self.controller.modulate_beam_pattern()
        self.assertTrue(-1.0 <= output <= 1.0)

if __name__ == "__main__":
    unittest.main()

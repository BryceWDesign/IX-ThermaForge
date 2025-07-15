"""
Unit tests for IX-ThermaForge triangular beam array module.
Author: Bryce Wooster
Date: 2025-07-15
"""

import unittest
from src.beam_shaping.triangular_beam_array import TriangularBeamArray
import math

class TestTriangularBeamArray(unittest.TestCase):
    def setUp(self):
        self.beam_array = TriangularBeamArray()

    def test_coherent_output_magnitude_phase(self):
        self.beam_array.set_phase(0, 0.0)
        self.beam_array.set_phase(1, 2.09)  # ~120 degrees
        self.beam_array.set_phase(2, 4.18)  # ~240 degrees
        magnitude, phase = self.beam_array.get_coherent_output()
        self.assertAlmostEqual(magnitude, 0.0, places=2)
        self.assertTrue(-math.pi <= phase <= math.pi)

    def test_phase_wrapping(self):
        self.beam_array.set_phase(0, 7.0)  # > 2π
        self.beam_array.update_phases(0.1)
        self.assertTrue(0 <= self.beam_array.beam_phases[0] <= 2 * math.pi)

if __name__ == "__main__":
    unittest.main()

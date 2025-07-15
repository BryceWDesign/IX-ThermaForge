"""
IX-ThermaForge Triangular Beam Array Module
Author: Bryce Wooster
Date: 2025-07-15

Description:
Controls the configuration and modulation of a three-port triangular beam output system.
Integrates beam shaping slits and phased control to unify beam edges into a coherent triangular output.

This module models the field-coherent combination of beams using real-world physics principles.
"""

import math
import numpy as np

class TriangularBeamArray:
    def __init__(self, base_wavelength_nm=900):
        """
        Initialize triangular beam array with a base wavelength.
        """
        self.base_wavelength_nm = base_wavelength_nm
        self.beam_phases = [0.0, 0.0, 0.0]  # phase per beam port

    def set_phase(self, port_index, phase_radians):
        """
        Set the phase for a specific beam port (0,1,2).
        """
        if 0 <= port_index < 3:
            self.beam_phases[port_index] = phase_radians

    def get_coherent_output(self):
        """
        Compute the coherent superposition of the three beams forming the triangular beam.
        """
        # Sum complex phasors for each beam
        phasors = [complex(math.cos(p), math.sin(p)) for p in self.beam_phases]
        combined_phasor = sum(phasors)

        # Normalize magnitude to max 1.0
        magnitude = abs(combined_phasor) / 3.0
        phase = math.atan2(combined_phasor.imag, combined_phasor.real)
        return magnitude, phase

    def update_phases(self, phase_shift_radians):
        """
        Increment all beam phases by a uniform phase shift.
        """
        for i in range(3):
            self.beam_phases[i] += phase_shift_radians
            # Wrap phases between 0 and 2π
            if self.beam_phases[i] > 2 * math.pi:
                self.beam_phases[i] -= 2 * math.pi

# Example test harness
if __name__ == "__main__":
    beam_array = TriangularBeamArray()
    beam_array.set_phase(0, 0.0)
    beam_array.set_phase(1, 2.09)  # 120 degrees in radians
    beam_array.set_phase(2, 4.18)  # 240 degrees in radians

    for step in range(100):
        mag, ph = beam_array.get_coherent_output()
        print(f"Step {step}: Magnitude={mag:.3f}, Phase={ph:.3f} rad")
        beam_array.update_phases(0.05)

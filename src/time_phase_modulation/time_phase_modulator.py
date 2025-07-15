"""
IX-ThermaForge Time-Phase Modulation Module
Author: Bryce Wooster
Date: 2025-07-15

Description:
Implements time-phase modulation algorithms based on Tesla 3-6-9 harmonic principles.
Enables fine tuning of time dilation/contraction effects through synchronized modulation cycles.

This module aims to support theoretical field warping and resonance effects consistent with real physics.
"""

import math
import time

class TimePhaseModulator:
    def __init__(self, base_frequency_hz=60.0):
        """
        Initialize the time-phase modulator with a base frequency.
        """
        self.base_frequency = base_frequency_hz
        self.phase = 0.0

    def get_harmonic_multiplier(self, t=None):
        """
        Cycles through Tesla's harmonic multiples 3, 6, 9 based on time.
        """
        if t is None:
            t = time.time()
        multipliers = [3, 6, 9]
        index = int(t) % 3
        return multipliers[index]

    def modulate(self, delta_time):
        """
        Apply modulation step over delta_time (seconds).
        Returns modulation value representing phase shift.
        """
        harmonic_multiplier = self.get_harmonic_multiplier()
        freq = self.base_frequency * harmonic_multiplier
        self.phase += freq * delta_time
        # Wrap phase between 0 and 2π
        if self.phase > 2 * math.pi:
            self.phase -= 2 * math.pi
        modulation_value = math.sin(self.phase)
        return modulation_value

# Example usage for testing
if __name__ == "__main__":
    modulator = TimePhaseModulator()
    prev_time = time.time()
    while True:
        current_time = time.time()
        delta = current_time - prev_time
        prev_time = current_time
        val = modulator.modulate(delta)
        print(f"Modulation: {val:.3f}")
        time.sleep(0.1)

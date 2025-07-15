"""
IX-ThermaForge Configuration Constants
Author: Bryce Wooster
Date: 2025-07-15

Description:
Centralized constants and configuration parameters for IX-ThermaForge modules.
Defines base frequencies, power limits, thermal thresholds, and harmonic multipliers.
"""

# Base system frequencies (Hz)
BASE_FREQUENCY_HZ = 60.0

# Harmonic multipliers used in Tesla 3-6-9 principles
HARMONIC_MULTIPLIERS = [3, 6, 9]

# Thermal management thresholds (degrees Celsius)
MAX_OPERATING_TEMPERATURE_C = 85.0
AMBIENT_TEMPERATURE_C = 25.0

# Power limits (kilowatts)
MAX_INPUT_POWER_KW = 500.0
MIN_INPUT_POWER_KW = 10.0

# Magnetic field base strength (Tesla)
BASE_MAGNETIC_FIELD_TESLA = 0.5

# Field stabilization base strength
BASE_FIELD_STRENGTH = 1.0

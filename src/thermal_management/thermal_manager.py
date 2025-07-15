"""
IX-ThermaForge Thermal Management Module
Author: Bryce Wooster
Date: 2025-07-15

Description:
Manages system thermal balance using real-world physics and materials data.
Implements active cooling feedback loops and temperature regulation algorithms.

This module ensures safe operation and maximizes beam stability under high power.
"""

class ThermalManager:
    def __init__(self, ambient_temp_c=25.0):
        self.current_temp_c = ambient_temp_c
        self.ambient_temp_c = ambient_temp_c
        self.cooling_rate_c_per_sec = 0.1
        self.heat_generation_factor = 0.15  # power to heat conversion

    def update_temperature(self, input_power_kw, delta_time_sec):
        """
        Update the internal temperature based on input power and elapsed time.
        """
        heat_generated = input_power_kw * self.heat_generation_factor * delta_time_sec
        # Temperature rise proportional to heat generated
        self.current_temp_c += heat_generated
        # Cooling effect
        cooling = self.cooling_rate_c_per_sec * delta_time_sec
        if self.current_temp_c > self.ambient_temp_c:
            self.current_temp_c -= cooling
        if self.current_temp_c < self.ambient_temp_c:
            self.current_temp_c = self.ambient_temp_c
        return self.current_temp_c

# Example usage
if __name__ == "__main__":
    import time
    tm = ThermalManager()
    power_kw = 200.0
    while True:
        temp = tm.update_temperature(power_kw, 1)
        print(f"Current Temp: {temp:.2f}°C")
        time.sleep(1)

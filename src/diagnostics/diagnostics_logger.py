"""
IX-ThermaForge Diagnostics and Logging Module
Author: Bryce Wooster
Date: 2025-07-15

Description:
Provides real-time diagnostics and logging for system health, performance, and error tracking.
Supports integration with core modules to monitor beam stability, thermal states, and field coherence.
"""

import logging
from ..utils.helpers import setup_logger

class DiagnosticsLogger:
    def __init__(self, name="IXThermaForgeDiagnostics"):
        self.logger = setup_logger(name)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_beam_status(self, modulation, power_kw, temperature_c):
        msg = f"Beam Modulation: {modulation:.3f}, Power: {power_kw:.2f} kW, Temp: {temperature_c:.2f} °C"
        self.log_info(msg)

# Example usage
if __name__ == "__main__":
    diag = DiagnosticsLogger()
    diag.log_info("Diagnostics logger initialized.")
    diag.log_beam_status(0.75, 200.0, 45.5)

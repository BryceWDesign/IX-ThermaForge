"""
IX-ThermaForge Utility Helper Functions
Author: Bryce Wooster
Date: 2025-07-15

Description:
Common utility functions used across IX-ThermaForge modules.
Includes mathematical helpers, logging utilities, and validation routines.
"""

import math
import logging

def clamp(value, min_value, max_value):
    """
    Clamp a value between a minimum and maximum.
    """
    return max(min_value, min(value, max_value))

def degrees_to_radians(deg):
    """
    Convert degrees to radians.
    """
    return deg * (math.pi / 180.0)

def radians_to_degrees(rad):
    """
    Convert radians to degrees.
    """
    return rad * (180.0 / math.pi)

def setup_logger(name, level=logging.INFO):
    """
    Setup and return a logger with specified name and level.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

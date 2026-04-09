"""
settings_example.py

Starter config structure for a gesture-controlled UR system.
Adapt to your real robot, camera, and safety rules.
"""

ROBOT_IP = "10.7.103.235"

# Motion
SPEED = 0.02
ACCELERATION = 0.10
WATCHDOG_S = 0.30

# Example workspace limits in meters
WORKSPACE_LIMITS = {
    "x_min": -0.60,
    "x_max": 0.60,
    "y_min": -0.60,
    "y_max": 0.60,
    "z_min": -0.05,
    "z_max": 0.35,
}
WORKSPACE_MARGIN = 0.05

# Example accepted robot/safety modes
SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example gesture confidence thresholds
CONFIDENCE_THRESHOLD = {
    "Right": 0.65,
    "Left": 0.80,
}

# Example debounce windows
DEBOUNCE_WINDOW = {
    "Right": 8,
    "Left": 10,
}

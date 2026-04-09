"""
vision_rtde_settings_example.py

Starter config structure for a vision + RTDE control project.
Adapt to your real robot, camera, and perception stack.
"""

ROBOT_IP = "10.7.103.235"

# Motion
SPEED = 0.02
ACCELERATION = 0.10
WATCHDOG_S = 0.30

# Example workspace limits
WORKSPACE_LIMITS = {
    "x_min": -0.60,
    "x_max": 0.60,
    "y_min": -0.60,
    "y_max": 0.60,
    "z_min": -0.05,
    "z_max": 0.35,
}
WORKSPACE_MARGIN = 0.05

# Example safe states
SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example vision confidence threshold
VISION_CONFIDENCE_THRESHOLD = 0.65

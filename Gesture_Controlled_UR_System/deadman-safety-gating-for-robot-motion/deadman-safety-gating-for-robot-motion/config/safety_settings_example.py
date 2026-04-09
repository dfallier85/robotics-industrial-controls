"""
safety_settings_example.py

Starter config for deadman and safety-gating logic.
Adapt these values to match your real robot and integration path.
"""

# Example allowed robot / safety modes
SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example digital input assignment
DEADMAN_DI = 0

# Example watchdog timeout in seconds
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

# Example motion settings
SPEED = 0.02
ACCELERATION = 0.10

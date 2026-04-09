"""
workspace_settings_example.py

Starter config for workspace limiting logic.
Adapt to your real robot and workcell.
"""

WORKSPACE_LIMITS = {
    "x_min": -0.60,
    "x_max": 0.60,
    "y_min": -0.60,
    "y_max": 0.60,
    "z_min": -0.05,
    "z_max": 0.35,
}

WORKSPACE_MARGIN = 0.05

# Example speed settings
SPEED = 0.02
ACCELERATION = 0.10

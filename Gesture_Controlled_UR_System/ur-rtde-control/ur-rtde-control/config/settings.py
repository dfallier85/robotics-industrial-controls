"""
settings.py

Starter config file for UR RTDE-based control projects.
Adapt these values to match your robot, workspace, and safety rules.
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

# Example safety expectations
SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example home joints in radians
HOME_JOINTS = [0.0, -1.57, 1.57, -1.57, -1.57, 0.0]

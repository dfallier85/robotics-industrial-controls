"""
deadman_settings_example.py

Starter config for physical deadman integration in a UR control project.
Adapt to your actual signal mapping and robot state logic.
"""

# Example digital input index used by the control logic
DEADMAN_DI = 0

# Example active state
DEADMAN_ACTIVE_STATE = True

# Example allowed robot/safety modes
SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example watchdog timeout
WATCHDOG_S = 0.30

# Example motion settings
SPEED = 0.02
ACCELERATION = 0.10

"""
watchdog_settings_example.py

Starter config for robot state monitoring and watchdog logic.
Adapt to your real robot and control loop.
"""

WATCHDOG_S = 0.30

SAFE_ROBOT_MODES = {7}
SAFE_SAFETY_MODES = {1}

# Example motion settings
SPEED = 0.02
ACCELERATION = 0.10

# Example state checks to log or watch
ENABLE_POSE_MONITORING = True
ENABLE_INPUT_MONITORING = True

"""
ur_rtde_control.py

Starter example for controlling a Universal Robots arm through RTDE in Python.

This script is intentionally simple and readable. It demonstrates:
- connecting to the robot
- checking connection/state basics
- sending a small speed command
- stopping cleanly

Before running:
- install the RTDE Python library you are using
- update ROBOT_IP
- verify safety conditions on the real robot
"""

import time

# These imports assume the ur_rtde package is installed.
# Common package name: ur-rtde
from rtde_control import RTDEControlInterface
from rtde_receive import RTDEReceiveInterface


ROBOT_IP = "10.7.103.235"

# Simple motion settings
SPEED = 0.02
ACCELERATION = 0.10
COMMAND_TIME = 1.0


def main():
    rtde_c = None
    rtde_r = None

    try:
        print(f"Connecting to UR robot at {ROBOT_IP}...")
        rtde_c = RTDEControlInterface(ROBOT_IP)
        rtde_r = RTDEReceiveInterface(ROBOT_IP)

        print("Connected.")
        print(f"Robot mode: {rtde_r.getRobotMode()}")
        print(f"Safety mode: {rtde_r.getSafetyMode()}")

        # Example Cartesian speed command: small +X motion.
        tcp_speed = [SPEED, 0.0, 0.0, 0.0, 0.0, 0.0]

        print("Sending speedL command...")
        rtde_c.speedL(tcp_speed, ACCELERATION, COMMAND_TIME)

        time.sleep(COMMAND_TIME)

        print("Stopping robot motion...")
        rtde_c.stopL(ACCELERATION)

        print("Done.")

    except Exception as exc:
        print(f"ERROR: {exc}")

    finally:
        try:
            if rtde_c is not None:
                rtde_c.stopScript()
        except Exception:
            pass


if __name__ == "__main__":
    main()

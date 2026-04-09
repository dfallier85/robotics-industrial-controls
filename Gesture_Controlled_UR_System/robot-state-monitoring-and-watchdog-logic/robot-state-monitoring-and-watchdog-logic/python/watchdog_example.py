"""
watchdog_example.py

A very small starter example showing the idea of command freshness and watchdog stop behavior.
This is not a full robot controller. It demonstrates the control logic pattern.

Replace the stop_robot_motion() stub with your real RTDE stop call in a real project.
"""

import time

WATCHDOG_S = 0.30
last_command_time = None
active_command = None


def update_command(command: str):
    global last_command_time, active_command
    active_command = command
    last_command_time = time.time()
    print(f"Command updated: {active_command}")


def command_is_fresh() -> bool:
    if last_command_time is None:
        return False
    return (time.time() - last_command_time) <= WATCHDOG_S


def stop_robot_motion():
    print("STOP: watchdog expired or command invalid")


def main():
    global active_command

    # Simulate a fresh command.
    update_command("+Y")

    for i in range(10):
        time.sleep(0.1)

        if command_is_fresh():
            print(f"Loop {i}: command still fresh -> {active_command}")
        else:
            print(f"Loop {i}: command stale")
            stop_robot_motion()
            active_command = None
            break


if __name__ == "__main__":
    main()

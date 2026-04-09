# Safety and Motion Notes

## Main point

RTDE motion control should be treated seriously.

Even small test motions should only be run when:
- workspace is clear
- the robot is in an appropriate state
- the commanded speed is intentionally low
- stop behavior is understood

## Starter motion choice

This repo uses a very small `speedL` example because it is easier to explain than a more complex control loop.

## Good future upgrades

- workspace limiting
- deadman input
- watchdog timeout
- safety state checks before motion
- stop logic on communication loss

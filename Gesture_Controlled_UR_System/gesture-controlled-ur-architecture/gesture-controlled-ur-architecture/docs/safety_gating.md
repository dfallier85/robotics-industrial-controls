# Safety Gating

## Main point

A gesture-recognition system should not command motion unless safety conditions allow it.

## Typical checks

- robot mode safe
- safety mode normal
- deadman input true
- workspace limit not violated
- command direction allowed at current position

## Why this matters

The resolver may ask for motion, but the safety gate has the final say.

That is how you keep the system from:
- moving when the robot is not ready
- pushing farther into a workspace boundary
- moving after a deadman is released

## Good future upgrades

- physical deadman input
- softer limit zones
- safety logs
- command suppression reasons

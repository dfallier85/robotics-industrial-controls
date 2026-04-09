# State Monitoring Concepts

## Main idea

A custom robot-control system should watch robot state continuously instead of assuming the state stays valid after startup.

## Why this matters

A robot may change state because of:
- operator action
- safety event
- communication issue
- protective stop
- mode change
- script shutdown

If the control loop does not observe those changes, it may keep acting on stale assumptions.

## Good rule

Before or during motion, ask:
- what is the robot state now?
- is motion still permitted?
- what changed since the last loop?

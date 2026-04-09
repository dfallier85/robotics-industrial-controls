# State Monitoring Notes

## Why state matters

Before moving the robot, you should know what state it is in.

Useful values often include:
- robot mode
- safety mode
- TCP pose
- actual joint positions
- digital input state

## Why this matters

A lot of better robot-control logic comes from reading state before commanding motion.

That is how you build:
- gating logic
- interlocks
- logging
- safer automation behavior

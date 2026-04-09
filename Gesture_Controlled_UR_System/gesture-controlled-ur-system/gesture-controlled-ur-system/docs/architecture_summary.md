# Architecture Summary

## Main flow

```text
Camera
 -> Gesture / Vision Processing
 -> Perception Result
 -> Command Resolver
 -> Safety Gate
 -> Workspace Limiter
 -> Watchdog / State Monitor
 -> Motion Dispatcher
 -> UR RTDE
```

## Main idea

The system is designed so that:
- vision creates intent
- safety decides permission
- motion dispatch happens only after validation

That separation is the main architectural strength of the project.

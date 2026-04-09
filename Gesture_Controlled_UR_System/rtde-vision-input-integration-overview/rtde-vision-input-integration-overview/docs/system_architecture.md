# System Architecture

## Basic Flow

```text
[Camera]
   ->
[Vision Processing]
   ->
[Perception Result]
   ->
[Intent Resolver]
   ->
[Safety / Validity Gate]
   ->
[Motion Dispatcher]
   ->
[UR RTDE]
```

## Why this split matters

The perception stack and motion stack have different jobs.

### Vision side
- interprets the scene
- produces a usable result

### Control side
- decides whether motion is permitted
- enforces safety and freshness
- sends actual robot commands

Keeping those separate makes the system easier to explain and debug.

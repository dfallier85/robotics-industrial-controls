# System Architecture

## Basic Vision-Guided Robotics Flow

```text
[Part / Workpiece]
        ->
[Lighting]
        ->
[Camera]
        ->
[Vision Controller]
        ->
[PLC / Robot Controller]
        ->
[Robot Action]
```

## Major Roles

### Camera
Captures the image of the workpiece or scene.

### Lighting
Controls image consistency. In real cells, lighting quality often decides whether the system is reliable.

### Vision Controller
Processes the image and produces:
- pass/fail result
- feature location
- orientation
- measurement
- classification result

### PLC
Often handles:
- sequence control
- interlocks
- handshake timing
- fault handling
- HMI status

### Robot
Uses the result to:
- pick
- place
- reject
- sort
- inspect another view
- stop or hold position

## Ownership Question

A key architecture choice is deciding who owns the sequence:

### PLC-centered
The PLC tells vision when to inspect and tells the robot what to do with the result.

### Robot-centered
The robot triggers the vision system and reacts directly to the returned result.

### Hybrid
The robot performs motion while the PLC manages safety, timing, and high-level decisions.

Hybrid is common in real industrial cells.

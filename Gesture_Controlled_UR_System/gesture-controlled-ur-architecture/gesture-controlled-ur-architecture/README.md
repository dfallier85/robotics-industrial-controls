# Gesture-Controlled UR Robot Architecture

A practical GitHub-style guide for organizing a gesture-controlled Universal Robots system.

This repo is written as a system architecture piece, not just a code dump.  
It explains how a gesture-control stack can be broken into clear layers so the system stays understandable, debuggable, and safer to evolve.

This is especially useful for projects combining:
- camera input
- gesture recognition
- command resolution
- RTDE robot control
- safety gating
- watchdog / shutdown behavior

---

## What This Project Covers

- high-level gesture control architecture
- separation of perception, command logic, and robot motion
- safety gating concepts
- watchdog and shutdown ideas
- suggested config structure
- event flow examples
- a reusable template for future gesture-control projects

---

## Why This Matters

A gesture-controlled robot is not just “camera in, robot moves.”

The real value is in how the system is structured:
- what detects the gesture
- what decides the command
- what blocks unsafe commands
- what actually sends motion
- what happens if the loop dies or tracking is lost

That is where the engineering lives.

---

## Folder Structure

```text
gesture-controlled-ur-architecture/
├── README.md
├── docs/
│   ├── system_architecture.md
│   ├── gesture_pipeline.md
│   ├── command_resolution.md
│   ├── safety_gating.md
│   ├── watchdog_and_shutdown.md
│   └── deployment_notes.md
├── examples/
│   ├── event_flow_example.md
│   └── module_split_example.md
├── config/
│   └── settings_example.py
├── templates/
│   └── gesture_robot_project_template.md
└── .gitignore
```

---

## High-Level System Idea

```text
[Camera]
   ->
[Gesture Detection / Tracking]
   ->
[Gesture Classification]
   ->
[Command Resolver]
   ->
[Safety Gate]
   ->
[Motion Dispatcher]
   ->
[UR RTDE Control]
```

That separation is what makes the project understandable and maintainable.

---

## Core Design Principle

Do **not** let raw perception talk directly to robot motion.

Instead, put clear layers in between:
- classifier
- resolver
- safety gate
- dispatcher

That way the system can:
- reject weak signals
- enforce workspace rules
- require deadman conditions
- stop cleanly on failure

---

## Typical Responsibilities by Layer

### Perception
- read camera frames
- detect hands
- track landmarks
- classify gestures

### Command Resolver
- map gestures to robot actions
- resolve conflicts
- decide when no command should be issued

### Safety Gate
- check robot state
- check safety mode
- check deadman condition
- check workspace limits
- suppress unsafe motion

### Motion Dispatcher
- convert approved command into motion call
- send RTDE motion
- stop on command loss or shutdown

---

## How to Use This Repo

Start with:
- `docs/system_architecture.md`
- `docs/gesture_pipeline.md`
- `docs/command_resolution.md`

Then review:
- `docs/safety_gating.md`
- `docs/watchdog_and_shutdown.md`
- `docs/deployment_notes.md`

Use:
- `examples/event_flow_example.md`
- `examples/module_split_example.md`
- `config/settings_example.py`

For future writeups:
- `templates/gesture_robot_project_template.md`

---

## Author Notes

This repo is intentionally architecture-focused.  
The point is to show how gesture control becomes a real robot-control system instead of just a demo.

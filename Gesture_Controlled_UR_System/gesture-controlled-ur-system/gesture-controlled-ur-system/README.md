# Gesture-Controlled UR System

A portfolio-level system overview for a gesture-controlled Universal Robots platform built around camera input, gesture interpretation, RTDE motion control, safety gating, workspace limiting, and watchdog behavior.

This repo is the **master project README layer** that ties together the supporting subprojects and explains the full system as one engineered robot-control stack.

---

## System Goal

Use camera-based gesture input to command a UR robot in a controlled way while preserving:

- motion intent separation
- safety gating
- deadman-based permission
- workspace limiting
- watchdog freshness
- controlled stop behavior

This is not meant to be “camera sees hand, robot moves instantly.”

It is designed as:

```text
Vision Input
    ->
Perception Result
    ->
Command Intent
    ->
Safety / Validity Checks
    ->
Motion Dispatcher
    ->
UR RTDE Control
```

That design choice is the whole point.

---

## Why This Project Matters

This system shows more than robot movement.

It shows how to integrate:

- perception
- command logic
- robot control
- safety gating
- motion boundaries
- failure handling

into one understandable architecture.

That makes it much stronger than a one-off motion demo.

---

## Included Project Stack

This master project is built from the following supporting repos:

### 1. RTDE Motion Foundation
- `ur-rtde-control`

Purpose:
- connect to the robot
- read robot state
- send controlled motion commands
- stop cleanly

---

### 2. Gesture System Architecture
- `gesture-controlled-ur-architecture`

Purpose:
- define the control stack
- separate perception, resolution, safety, and motion
- explain how the gesture system is organized

---

### 3. Motion Permission / Safety Layer
- `deadman-safety-gating-for-robot-motion`
- `physical-deadman-integration-for-ur-control`

Purpose:
- require live enable conditions
- block motion when deadman is false
- define clear motion-permission logic

---

### 4. Spatial Control Layer
- `workspace-limiting-and-motion-inhibition`

Purpose:
- keep motion inside a defined workspace
- suppress unsafe direction components
- avoid pushing farther into restricted bounds

---

### 5. Health / Reliability Layer
- `robot-state-monitoring-and-watchdog-logic`

Purpose:
- monitor robot state
- enforce command freshness
- stop on stale commands or control-loop failure

---

### 6. Vision-to-Control Integration Layer
- `rtde-vision-input-integration-overview`

Purpose:
- connect visual input to command intent
- explain how vision results should influence motion without bypassing the rest of the control system

---

## High-Level Architecture

```text
[Camera]
   ->
[Gesture / Vision Processing]
   ->
[Perception Result]
   ->
[Command Resolver]
   ->
[Safety Gate]
   ->
[Workspace Limiter]
   ->
[Watchdog / State Monitor]
   ->
[Motion Dispatcher]
   ->
[UR RTDE]
```

Not every layer has to be a separate process, but each layer should have a clear role.

---

## Key Design Principles

### 1. Perception is not motion
The vision system should produce a useful interpretation of the scene, not directly command the robot.

### 2. Intent is separate from permission
The resolver may ask for motion.  
The safety system decides whether motion is allowed.

### 3. Safe motion should degrade predictably
If a condition becomes invalid, the system should:
- block motion
- suppress unsafe components
- or stop cleanly

### 4. Freshness matters
A stale gesture or stale command should not keep the robot moving.

### 5. State matters
Robot mode, safety mode, input state, and pose should all influence motion permission.

---

## Typical Flow Example

### Scenario: right-hand gesture requests +Y motion

1. camera captures frame
2. gesture pipeline classifies a known gesture
3. resolver maps that gesture to `move +Y`
4. safety gate checks:
   - robot mode
   - safety mode
   - deadman state
5. workspace limiter checks whether `+Y` is still allowed
6. watchdog confirms command freshness
7. dispatcher sends approved motion through RTDE
8. if gesture disappears or deadman drops, motion stops

---

## Failure Handling Philosophy

A strong system is not only defined by how it moves.

It is also defined by how it stops.

This project is built around explicit handling for cases like:
- deadman released
- stale command
- loop failure
- robot mode not allowed
- safety mode not allowed
- motion requested near workspace boundary

The goal is to make those cases explainable, not mysterious.

---

## Suggested Folder Grouping

If you want to package the whole system together, a clean layout is:

```text
gesture-controlled-ur-system/
├── README.md
├── docs/
│   ├── architecture_summary.md
│   ├── deployment_summary.md
│   └── validation_summary.md
├── ur-rtde-control/
├── gesture-controlled-ur-architecture/
├── deadman-safety-gating-for-robot-motion/
├── physical-deadman-integration-for-ur-control/
├── workspace-limiting-and-motion-inhibition/
├── robot-state-monitoring-and-watchdog-logic/
└── rtde-vision-input-integration-overview/
```

This master repo gives reviewers one clear entry point instead of forcing them to guess how the subprojects relate.

---

## What to Emphasize in a Portfolio

When talking about this system, focus on:

- custom robot control through RTDE
- gesture-driven command generation
- separation between perception and motion
- deadman-based motion permission
- workspace-aware inhibition
- watchdog stop behavior
- safe handling of stale or invalid input

Those are the points that make this feel like an engineered system instead of a novelty.

---

## Validation Priorities

A project like this should prove not only that it moves, but that it behaves correctly when conditions change.

Good validation topics include:

- gesture recognized correctly
- intended motion command generated
- deadman required for motion
- workspace limit suppresses unsafe direction
- stale input triggers stop
- safety state blocks motion
- shutdown path stops cleanly

---

## Good Future Expansions

This system can naturally grow into:

- richer gesture sets
- logged operator sessions
- visual status overlays
- PLC or external interlock integration
- more formal safety-state reporting
- multi-modal control inputs
- robot / vision state dashboards

---

## Author Notes

This repo is intentionally a master overview, not a duplicate of all subproject content.

Its purpose is to:
- explain the full gesture-controlled UR system
- connect the supporting repos
- make the project understandable as one architecture
- give the portfolio a strong central entry point

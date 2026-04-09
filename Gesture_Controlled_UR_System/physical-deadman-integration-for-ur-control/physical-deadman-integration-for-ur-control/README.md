# Physical Deadman Integration for UR Control

A practical GitHub-style guide for integrating a physical deadman input into a Universal Robots control workflow.

This repo is written as a system design and implementation reference for projects where robot motion should only be permitted while a real hardware enable condition is held.

It is useful for systems involving:
- UR RTDE motion control
- custom Python robot control loops
- gesture-based motion control
- robot digital inputs
- external enable devices
- state-based motion permission

---

## What This Project Covers

- why a physical deadman matters
- where a deadman signal can enter the control chain
- how motion permission should depend on a live enable input
- interaction with RTDE state monitoring
- input mapping and signal interpretation
- example configuration structure
- reusable documentation templates

---

## Why This Matters

A physical deadman is a much stronger control concept than a purely software-held enable flag.

It creates a clearer rule:

- no held deadman
- no motion

That makes the control system more intentional, easier to reason about, and closer to real operator-enable patterns used in industrial environments.

---

## Folder Structure

```text
physical-deadman-integration-for-ur-control/
├── README.md
├── docs/
│   ├── deadman_role.md
│   ├── input_signal_path.md
│   ├── ur_input_monitoring.md
│   ├── motion_permission_logic.md
│   ├── failure_and_drop_behavior.md
│   └── testing_and_validation.md
├── examples/
│   ├── signal_flow_example.md
│   └── drop_deadman_case_example.md
├── config/
│   └── deadman_settings_example.py
├── templates/
│   └── deadman_integration_project_template.md
└── .gitignore
```

---

## Core Design Idea

A physical deadman should be treated as an input to the motion-permission layer:

```text
[Command Intent]
      ->
[Robot State + Deadman Input Check]
      ->
[Motion Permission]
      ->
[Dispatcher]
      ->
[UR Robot]
```

The command source may request motion.

The deadman input helps decide whether motion is actually allowed right now.

---

## Typical Integration Path

A common pattern is:

1. deadman device is wired to a real input path
2. the robot or associated control system reports that input state
3. the control loop reads the input state
4. motion is allowed only while the input is active

That keeps the enable path tied to a real physical condition instead of a stale software assumption.

---

## How to Use This Repo

Start with:
- `docs/deadman_role.md`
- `docs/input_signal_path.md`
- `docs/ur_input_monitoring.md`

Then review:
- `docs/motion_permission_logic.md`
- `docs/failure_and_drop_behavior.md`
- `docs/testing_and_validation.md`

Examples:
- `examples/signal_flow_example.md`
- `examples/drop_deadman_case_example.md`

Config starter:
- `config/deadman_settings_example.py`

For future projects:
- `templates/deadman_integration_project_template.md`

---

## Author Notes

This repo is intentionally architecture-focused.  
The goal is to show how a physical enable signal should influence motion permission in a UR control system instead of being treated like an afterthought.

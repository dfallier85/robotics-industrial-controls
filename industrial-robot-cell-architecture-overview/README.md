# Industrial Robot Cell Architecture Overview

A practical GitHub-style guide for understanding and documenting the architecture of an industrial robot cell.

This repo is written as a system-level overview for how the major pieces of a robot cell fit together:
- robot
- PLC
- safety
- HMI
- vision
- conveyors / tooling
- network / communication layers
- diagnostics and fault handling

It is meant to help explain not just *what* equipment exists, but *how the cell behaves as a system*.

---

## What This Project Covers

- major layers inside an industrial robot cell
- ownership of machine sequencing vs robot execution
- safety and interlock structure
- vision and sensor integration
- PLC, HMI, and robot role separation
- fault and recovery thinking
- example signal and data flow
- reusable templates for future cell documentation

---

## Why This Matters

A robot cell is not just:
- a robot
- a PLC
- a few wires

It is a coordinated system with:
- control layers
- communication layers
- safety layers
- machine states
- operator interaction
- recovery behavior

Being able to describe that clearly is a strong engineering skill.

---

## Folder Structure

```text
industrial-robot-cell-architecture-overview/
├── README.md
├── docs/
│   ├── system_layers.md
│   ├── control_ownership.md
│   ├── safety_and_interlocks.md
│   ├── communications_and_networking.md
│   ├── operator_and_hmi.md
│   ├── vision_and_sensors.md
│   └── fault_recovery_and_diagnostics.md
├── examples/
│   ├── cell_signal_flow_example.md
│   └── pick_place_cell_example.md
├── templates/
│   └── robot_cell_project_template.md
└── .gitignore
```

---

## High-Level Cell View

```text
[Operator / HMI]
       |
       v
      [PLC]
   /    |    \
  /     |     \
 v      v      v
[Robot] [Vision] [Machine I/O]
   |                |
   v                v
[Tooling / EOAT]  [Conveyors / Fixtures / Sensors]
```

On top of this, you usually also have:
- safety circuits
- network communication
- fault handling
- startup / reset / recovery logic

---

## Core Design Idea

A good cell architecture clearly defines:

- who owns sequencing
- who owns motion
- who owns safety state
- who owns operator interaction
- how equipment reports status and faults
- how the cell returns to a valid running state after interruption

That is what makes the cell understandable.

---

## Typical Role Separation

### PLC
- owns machine sequence
- coordinates stations
- evaluates permissives and interlocks
- issues commands to robot and other equipment
- manages machine-level status

### Robot
- owns robot motion execution
- runs path or task logic
- reports robot status, busy, done, faults

### HMI
- provides operator interaction
- displays machine state
- displays faults and reset actions

### Vision system
- provides inspection, detection, or positional input
- reports results to PLC and/or robot

### Safety layer
- governs whether motion or automatic operation is permitted at all

---

## How to Use This Repo

Start with:
- `docs/system_layers.md`
- `docs/control_ownership.md`
- `docs/safety_and_interlocks.md`

Then review:
- `docs/communications_and_networking.md`
- `docs/operator_and_hmi.md`
- `docs/vision_and_sensors.md`
- `docs/fault_recovery_and_diagnostics.md`

Examples:
- `examples/cell_signal_flow_example.md`
- `examples/pick_place_cell_example.md`

For future projects:
- `templates/robot_cell_project_template.md`

---

## Author Notes

This repo is intentionally system-focused.  
The goal is to make an industrial robot cell understandable as a coordinated machine system instead of a collection of unrelated components.

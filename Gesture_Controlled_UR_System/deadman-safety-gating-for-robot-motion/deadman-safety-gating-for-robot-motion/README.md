# Deadman / Safety Gating for Robot Motion

A practical GitHub-style guide for structuring deadman logic and safety gating in robot-motion systems.

This repo is written as a system design and implementation reference for projects where robot motion should only be allowed when a clear enabling condition is present.

It is useful for systems involving:
- RTDE robot control
- gesture-controlled motion
- custom Python motion loops
- physical deadman switches
- state-based motion gating
- workspace-aware command suppression

---

## What This Project Covers

- what a deadman condition is in a robot-control system
- how to structure safety gating before motion commands are sent
- separation between intent and permission
- physical vs software deadman concepts
- suppression of unsafe commands
- example config structure
- reusable design template for future motion-control projects

---

## Why This Matters

A motion-control system should not move just because it *can*.

It should move only when:
- the robot is in an allowed state
- the safety state is acceptable
- the deadman is active
- the command direction is allowed
- the system is still alive and updating

That is the difference between “motion code” and a real control system.

---

## Folder Structure

```text
deadman-safety-gating-for-robot-motion/
├── README.md
├── docs/
│   ├── deadman_concepts.md
│   ├── safety_gate_architecture.md
│   ├── command_suppression.md
│   ├── physical_deadman_integration.md
│   ├── watchdog_interaction.md
│   └── testing_and_validation.md
├── examples/
│   ├── gating_flow_example.md
│   └── suppression_reason_example.md
├── config/
│   └── safety_settings_example.py
├── templates/
│   └── safety_gating_project_template.md
└── .gitignore
```

---

## Core Design Idea

Keep these layers separate:

```text
[Command Intent]
      ->
[Safety Gate]
      ->
[Motion Dispatcher]
```

The command layer may request motion.

The safety gate decides whether motion is permitted.

That separation is one of the most important design choices in a robot-motion system.

---

## Typical Safety Gate Inputs

A useful safety gate may check:

- robot mode
- safety mode
- deadman input
- workspace limit direction
- watchdog freshness
- optional interlock or enable bits

Only when those checks pass should a motion command be released to the dispatcher.

---

## Typical Outcomes

The safety gate should support outcomes like:

- allow command
- block command
- zero one motion axis only
- stop motion immediately
- return a reason for suppression

That makes troubleshooting much easier.

---

## How to Use This Repo

Start with:
- `docs/deadman_concepts.md`
- `docs/safety_gate_architecture.md`
- `docs/command_suppression.md`

Then review:
- `docs/physical_deadman_integration.md`
- `docs/watchdog_interaction.md`
- `docs/testing_and_validation.md`

Examples:
- `examples/gating_flow_example.md`
- `examples/suppression_reason_example.md`

Config starter:
- `config/safety_settings_example.py`

For future projects:
- `templates/safety_gating_project_template.md`

---

## Author Notes

This repo is intentionally architecture-focused.  
The goal is to show how to design motion permission logic that is clear, reusable, and safer than sending raw commands directly to the robot.

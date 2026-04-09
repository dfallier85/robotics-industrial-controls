# PLC ↔ Robot Communication (Clean Version)

A practical GitHub-style guide for building a clean PLC-to-robot communication layer for industrial systems.

This repo is written as a structured reference for communication between a PLC and one or more robots using:
- command words / bytes
- status bits
- acknowledgments
- handshakes
- interlocks
- timeouts
- transport-independent logic

It is meant to make PLC ↔ robot communication look like an engineered interface instead of a pile of tags.

---

## What This Project Covers

- communication architecture between PLC and robot
- command / acknowledgment handshake design
- status and fault reporting patterns
- command byte / word ideas
- timeout and retry thinking
- clean tag naming concepts
- starter Structured Text examples
- reusable template for future robot-cell projects

---

## Why This Matters

Real robot integration is not just motion programming.

A lot of real industrial value comes from:
- getting the PLC and robot to talk cleanly
- making commands obvious
- making responses trustworthy
- making faults diagnosable
- making the interface scalable to multiple cells

That is what this repo is about.

---

## Folder Structure

```text
plc-robot-communication-clean/
├── README.md
├── docs/
│   ├── architecture_overview.md
│   ├── command_handshake.md
│   ├── status_and_faults.md
│   ├── timeout_and_retry.md
│   └── naming_and_scaling.md
├── plc/
│   ├── structured_text_handshake_example.st
│   └── tag_map_example.md
├── examples/
│   ├── command_lifecycle_example.md
│   └── multi_robot_expansion_example.md
├── templates/
│   └── plc_robot_project_template.md
└── .gitignore
```

---

## Core Design Idea

Keep the communication interface clear:

```text
[HMI / Supervisor]
        ->
      [PLC]
        ->
[Command + Valid + Handshake]
        ->
     [Robot Cell]
        ->
[ACK + Status + Faults]
        ->
      [PLC]
```

The PLC should own the machine-level sequence.
The robot should own robot-level action execution.
The handshake between them should be boring, explicit, and easy to troubleshoot.

---

## Common Interface Pieces

A clean PLC ↔ robot interface often includes:

- command value
- command valid / active bit
- acknowledgement bit
- busy bit
- done bit
- fault bit
- optional response / status word
- timeout logic

That structure works across many robot brands and cells.

---

## How to Use This Repo

Start with:
- `docs/architecture_overview.md`
- `docs/command_handshake.md`

Then review:
- `docs/status_and_faults.md`
- `docs/timeout_and_retry.md`
- `docs/naming_and_scaling.md`

Use:
- `plc/structured_text_handshake_example.st`
- `plc/tag_map_example.md`

Examples:
- `examples/command_lifecycle_example.md`
- `examples/multi_robot_expansion_example.md`

For future projects:
- `templates/plc_robot_project_template.md`

---

## Author Notes

This repo is intentionally clean and transport-agnostic.  
The point is to document a good PLC ↔ robot communication pattern that can be adapted to Allen-Bradley, AS-i, Ethernet/IP, Modbus, or similar integrations.

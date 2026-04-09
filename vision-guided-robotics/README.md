# Vision-Guided Robotics: Keyence + Robot Integration Overview

A practical GitHub-style guide for explaining how a machine vision system can be integrated with an industrial robot for inspection, part location, pass/fail decisions, and robot motion logic.

This repo is written as a system-level portfolio piece. It is not tied to one exact cell layout, because the bigger value is understanding the architecture, signal flow, and integration decisions that make vision-guided robotics work in the real world.

---

## What This Project Covers

- Basic vision-guided robotics architecture
- How a Keyence vision controller fits into a robot cell
- Common communication paths between vision, robot, and PLC
- Typical workflow from image acquisition to robot action
- Practical integration considerations
- Example signal mapping and handshaking ideas
- A repeatable template for future VGR projects

---

## Why This Matters

This kind of project shows system understanding, not just coding.

It proves you can think about:
- cameras
- lighting
- inspection logic
- communications
- robot actions
- PLC coordination
- fault handling
- production realism

That reads much stronger than “I used a camera with a robot.”

---

## Folder Structure

```text
vision-guided-robotics/
├── README.md
├── docs/
│   ├── system_architecture.md
│   ├── integration_workflow.md
│   ├── communication_patterns.md
│   └── deployment_notes.md
├── examples/
│   ├── io_signal_example.md
│   └── pass_fail_pick_sequence.md
├── templates/
│   └── vgr_project_template.md
└── .gitignore
```

---

## Typical Hardware Stack

Example components in a VGR cell:

- Robot arm
- End effector / gripper
- Camera
- Vision controller
- Lighting
- PLC
- Safety hardware
- Fixture or conveyor
- HMI

### Example equipment you may see in this style of system
- Keyence CV-X series vision controller
- Keyence industrial camera
- Universal Robots, ABB, or FANUC robot
- PLC for sequencing and interlocks

---

## High-Level Architecture

```text
[Part / Scene]
      |
      v
[Lighting + Camera]
      |
      v
[Keyence Vision Controller]
      |
      | result / position / pass-fail
      v
[PLC and/or Robot Controller]
      |
      v
[Robot Motion / Handling Decision]
```

In some cells, the vision controller talks directly to the robot.  
In others, the PLC sits in the middle and manages the handshake.

---

## Common VGR Use Cases

- Presence / absence check
- Part orientation confirmation
- Pass / fail inspection
- Pick location guidance
- Sorting good vs bad parts
- Kit verification
- Label or mark inspection
- Feature measurement before robot action

---

## Core Integration Question

The real question is not just “can the camera find the part?”

It is:

**How does the result get turned into a safe, repeatable robot action?**

That is where a lot of real engineering value lives.

---

## Two Common Integration Styles

### 1. Inspection-driven robotics
The vision system decides whether the part passes inspection.

Then the robot:
- picks good parts
- rejects bad parts
- sorts by condition
- continues or stops the cycle

### 2. Position-guided robotics
The vision system returns location data.

Then the robot:
- offsets its motion
- moves to the reported position
- performs pick/place based on detected part location

---

## Main Design Decisions

When building or documenting a VGR system, answer these:

1. What does the camera need to detect?
2. Is the result binary, measured, or positional?
3. Does the PLC own the sequence, or does the robot?
4. How are pass/fail or coordinates transferred?
5. What happens if vision fails?
6. What happens if no part is found?
7. How is the operator informed?
8. How is the system re-taught or adjusted later?

---

## Practical Challenges

A lot of weak vision demos ignore these. Real systems do not.

### Lighting
Lighting often matters more than the camera itself.

### Repeatability
If the part presentation changes too much, vision performance drops.

### Timing
The vision cycle must fit the robot cycle.

### Communications
The result must be transferred cleanly and predictably.

### Fault Recovery
You need a defined behavior for:
- no result
- bad image
- communication timeout
- inspection fail
- robot unable to complete commanded motion

---

## Suggested Documentation Pattern

For each VGR project, document:

- goal
- hardware used
- camera location
- lighting setup
- what is being detected
- communication method
- robot response
- PLC logic involvement
- fail states
- operator actions
- future improvements

---

## How to Use This Repo

Start with:
- `docs/system_architecture.md`
- `docs/integration_workflow.md`

Then use:
- `docs/communication_patterns.md`
- `docs/deployment_notes.md`

For examples:
- `examples/io_signal_example.md`
- `examples/pass_fail_pick_sequence.md`

For future projects:
- `templates/vgr_project_template.md`

---

## Author Notes

This repo is meant to help turn VGR experience into a clean, repeatable explanation that looks strong in a portfolio and is useful for future project writeups.

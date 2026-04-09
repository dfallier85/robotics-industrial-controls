# UR RTDE Control with Python

A practical GitHub-style guide for controlling a Universal Robots arm using RTDE from Python.

This is a strong portfolio project because it shows direct robot control at the real motion layer, not just UI or MQTT plumbing.

It is useful for:
- motion control experiments
- gesture-based robot control
- safety-gated control logic
- robot state monitoring
- custom real-time-ish control loops

---

## What This Project Covers

- connecting to a UR robot using RTDE
- reading robot mode and safety mode
- sending a simple `speedL` command
- stopping motion cleanly
- organizing project settings for safer reuse
- a template for larger RTDE-based robot projects

---

## Why This Matters

This is one of the most serious robot-control layers in your portfolio.

It turns:
- "I can send a robot a command"

into:

- "I can connect to the robot's control and receive interfaces, monitor state, and drive motion intentionally"

That reads much stronger to anyone looking for robotics depth.

---

## Folder Structure

```text
ur-rtde-control/
├── README.md
├── python/
│   └── ur_rtde_control.py
├── config/
│   └── settings.py
├── docs/
│   ├── setup_notes.md
│   ├── safety_and_motion_notes.md
│   ├── state_monitoring_notes.md
│   └── testing_workflow.md
├── templates/
│   └── ur_rtde_project_template.md
└── .gitignore
```

---

## Requirements

- Universal Robots arm reachable on the network
- Python 3
- RTDE Python library compatible with your setup

Typical package name:

```bash
pip3 install ur-rtde
```

---

## Example Capabilities

This starter repo demonstrates:
- RTDE control connection
- RTDE receive connection
- reading robot and safety modes
- issuing a small Cartesian speed command
- stopping motion

Larger projects built from this pattern can add:
- gesture input
- watchdog logic
- workspace limiting
- deadman logic
- state logging
- dashboard integration

---

## Safety Reminder

Do not run robot motion code casually on a real robot.

Before using RTDE motion control on hardware:
- verify your robot IP
- verify your speed/acceleration settings
- confirm clear workspace
- confirm correct mode and safety state
- follow site safety rules

This repo is a starter reference, not permission to skip safe setup.

---

## Run

```bash
python3 python/ur_rtde_control.py
```

---

## How to Use This Repo

Start with:
- `docs/setup_notes.md`
- `docs/safety_and_motion_notes.md`
- `docs/state_monitoring_notes.md`
- `docs/testing_workflow.md`

Then update:
- `config/settings.py`
- `python/ur_rtde_control.py`

Use:
- `templates/ur_rtde_project_template.md`

for future RTDE-based robot projects.

---

## Author Notes

This repo is intentionally simple and readable. It is meant to be the clean base layer for more advanced UR RTDE control work.

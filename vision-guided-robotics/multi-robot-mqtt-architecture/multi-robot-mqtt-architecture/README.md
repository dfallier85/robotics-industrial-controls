# Multi-Robot MQTT Architecture: UR + ABB + PLC Integration

A GitHub-style system guide for controlling multiple industrial robots through a shared MQTT architecture, with a PLC included for command coordination, interlocks, and status handling.

This repo is written as a portfolio-ready architecture piece.  
It is meant to explain how a multi-robot communication stack can be designed so that:
- commands are organized cleanly
- each robot has its own topics
- responses are easy to interpret
- the PLC can participate in the system without turning the design into a mess

---

## What This Project Covers

- A scalable MQTT topic structure for multiple robots
- How Node-RED, MQTT, Python bridges, robots, and PLC logic fit together
- Separation of command topics and response topics
- A clean strategy for adding more robots later
- How PLC interlocks can be layered into the architecture
- Example topic mapping and example bridge behavior
- A reusable template for future multi-robot systems

---

## Why This Matters

This is the kind of system-level project that shows integration thinking.

It proves you can think beyond one robot and design something that is:
- structured
- debuggable
- expandable
- useful in a real controls environment

That is stronger than a one-off demo.

---

## Folder Structure

```text
multi-robot-mqtt-architecture/
├── README.md
├── docs/
│   ├── system_architecture.md
│   ├── topic_strategy.md
│   ├── plc_integration_notes.md
│   └── fault_handling.md
├── examples/
│   ├── topic_map_example.md
│   ├── node_red_flow_pattern.md
│   └── command_lifecycle_example.md
├── python/
│   └── multi_robot_bridge_example.py
├── nodered/
│   └── flow_pattern.json
├── templates/
│   └── multi_robot_project_template.md
└── .gitignore
```

---

## High-Level Architecture

```text
[Node-RED Dashboard / UI]
            |
            v
       [MQTT Broker]
        /    |    \
       /     |     \
      v      v      v
 [UR Bridge] [ABB Bridge] [PLC Bridge / PLC Interface]
      |          |               |
      v          v               v
 [UR Robot]  [ABB Robot]   [PLC Logic / Interlocks]
```

In this structure:
- each robot gets its own command topic
- each robot gets its own response topic
- the PLC can publish status, interlocks, or faults
- Node-RED can stay at the top as a clean operator-facing layer

---

## Recommended Topic Pattern

### UR
- `robot/ur/cmd`
- `robot/ur/response`

### ABB
- `robot/abb/cmd`
- `robot/abb/response`

### PLC
- `system/plc/status`
- `system/plc/fault`
- `system/plc/interlock`

### Optional shared supervisory topics
- `system/all/status`
- `system/all/fault`
- `system/all/cmd`

This keeps command ownership clear and makes debugging much easier.

---

## Design Principles

### 1. Keep each robot on its own command path
Do not dump all robot commands into one vague topic unless you have a very good reason.

### 2. Separate commands from responses
Command topics and response topics should not be mixed.

### 3. Use boring names
Clear topic names are better than clever ones.

### 4. Let the PLC own machine-level interlocks
The PLC is usually the right place for:
- safe sequencing
- permissives
- readiness checks
- cell-level interlocks
- alarm states

### 5. Keep Node-RED operator-friendly
Node-RED should be easy to read from the top down:
- send command
- receive response
- display state
- show alarms

---

## Typical Use Cases

- Send a `wave` command to UR
- Send a `home` command to ABB
- Show PLC interlock status in Node-RED
- Block robot action if a PLC permissive is false
- Return robot responses to the UI
- Expand later to more robot brands or subsystems

---

## How to Use This Repo

Start with:
- `docs/system_architecture.md`
- `docs/topic_strategy.md`

Then review:
- `docs/plc_integration_notes.md`
- `docs/fault_handling.md`

For examples:
- `examples/topic_map_example.md`
- `examples/node_red_flow_pattern.md`
- `examples/command_lifecycle_example.md`

If you want a starter code reference:
- `python/multi_robot_bridge_example.py`
- `nodered/flow_pattern.json`

Use:
- `templates/multi_robot_project_template.md`

to document future multi-robot projects in the same format.

---

## Author Notes

This repo is intentionally written as a system architecture guide instead of pretending there is only one “correct” implementation.  
The real value here is the structure, signal ownership, and expandability.

# PLC-to-Robot Handshake Using an 8-Bit Command Byte and ACK Toggle

A practical guide for building a simple and scalable handshake between a PLC and an industrial robot using an 8-bit command value, a command-valid bit, and a toggled ACK bit.

This project is based on a real multi-cell controls concept where different robot cells can be targeted from a PLC, commanded with a byte value, and confirmed through an ACK edge rather than a fixed ACK state.

---

## Overview

This approach is useful when you want a PLC to send commands to a robot cell in a clean and repeatable way without building a separate hardcoded tag for every single command.

Instead of using many individual command bits, the PLC sends:

- a target selector
- a command-valid bit
- an 8-bit command code
- and watches for an ACK edge from the robot side

This keeps the interface compact and makes it easier to expand later.

---

## What This Project Does

- Sends a command from a PLC to a robot cell
- Uses a single command byte (`USINT`) for command values
- Uses a `Cmd_Valid` bit to mark a command as active
- Watches an ACK bit for either a rising or falling edge
- Clears the active command after the ACK is detected
- Tracks timeout behavior if no ACK is received in time
- Leaves room for heartbeat monitoring and multi-robot expansion

---

## Why Use This Method

### Benefits

- Fewer tags than one-bit-per-command designs
- Easier to scale to multiple robots or machines
- Cleaner HMI and PLC logic
- Easy to document
- Good foundation for industrial integration work

### Core Idea

The robot does not have to hold ACK high forever.

It only needs to toggle the ACK bit when it has accepted or completed the command.  
The PLC only cares that the bit changed state.

That means:
- `0 -> 1` is valid
- `1 -> 0` is also valid

This makes the handshake more reliable than waiting for one exact level.

---

## System Architecture

```text
          [HMI / Supervisor Logic]
                    |
                    v
                 [PLC]
                    |
                    | Command Byte + Valid Bit
                    v
            [AS-i / Field I/O Layer]
                    |
                    v
                [Robot Cell]
                    |
                    | ACK Toggle Bit
                    v
                 [PLC Logic]
```

---

## Signal Example

| Signal Name | Type | Direction | Purpose |
|---|---|---:|---|
| `Cmd_Target` | `USINT` | PLC -> cell | Which cell should receive the command |
| `Cmd_Code` | `USINT` | PLC -> cell | The command number |
| `Cmd_Valid` | `BOOL` | PLC -> cell | Marks command as active |
| `Fanuc_Cmd` | `USINT` | PLC -> Fanuc | Copied command byte for Fanuc |
| `Fanuc_Cmd_Active` | `BOOL` | PLC internal | Fanuc command currently active |
| `Fanuc_ACK` | `BOOL` | Robot -> PLC | ACK bit returned from robot |
| `Fanuc_Ack_Last` | `BOOL` | PLC internal | Last scanned ACK state |
| `Fanuc_Ack_Edge` | `BOOL` | PLC internal | True when ACK changes state |
| `Fanuc_NoAck_Count` | `INT` | PLC internal | Timeout counter |
| `Fanuc_Tx_Timeout` | `BOOL` | PLC internal | True when no ACK arrives |

---

## Example Command Values

| Command Code | Meaning |
|---:|---|
| `1` | Reset |
| `2` | Home |
| `3` | Start Cycle |
| `4` | Stop Cycle |
| `5` | Open Gripper |
| `6` | Close Gripper |

Use whatever command list fits your cell.

---

## Project Folder Structure

```text
plc-robot-handshake-asi/
├── README.md
├── plc/
│   └── structured_text_example.st
├── examples/
│   └── command_map.csv
├── docs/
│   └── handshake_notes.md
└── .gitignore
```

---

## Handshake Sequence

### 1. PLC loads command

The PLC decides which robot should receive the command and writes:

- `Cmd_Target`
- `Cmd_Code`
- `Cmd_Valid = TRUE`

If the target matches Fanuc, for example:

- `Fanuc_Cmd := Cmd_Code`
- `Fanuc_Cmd_Active := TRUE`

### 2. Robot sees the command

The robot side reads the command byte and valid bit.

### 3. Robot accepts or finishes command

The robot toggles its ACK output bit.

### 4. PLC detects ACK edge

The PLC compares:

- current ACK state
- previous ACK state

If they are different, an ACK edge happened.

### 5. PLC clears command

The PLC resets:

- `Fanuc_Cmd_Active := FALSE`
- timeout counter
- command valid if needed

---

## Timeout Strategy

A command should not stay active forever.

A timeout counter gives the PLC a way to detect when the robot never acknowledged the command.

Example:
- PLC task runs every 20 ms
- Timeout threshold = 25 scans
- Total timeout = 500 ms

If no ACK edge happens before that:
- set `Fanuc_Tx_Timeout := TRUE`
- raise alarm or retry logic

---

## Heartbeat Strategy

A heartbeat bit helps confirm communication is still alive.

A simple pattern:
- toggle heartbeat every 500 ms in the PLC
- map it to a reserved output bit, such as bit 15
- do not overlap it with the 8-bit command space

This avoids collisions between command data and communication-health logic.

---

## Structured Text Example

See: [`plc/structured_text_example.st`](plc/structured_text_example.st)

This example shows:
- command latch logic
- ACK edge detection
- timeout counting
- heartbeat toggling

---

## How to Test

1. Force or write a command into `Cmd_Code`
2. Set `Cmd_Target` to the correct cell
3. Set `Cmd_Valid := TRUE`
4. Watch `Fanuc_Cmd` and `Fanuc_Cmd_Active`
5. Toggle the incoming `Fanuc_ACK` bit
6. Confirm the PLC detects the edge
7. Confirm the active command resets
8. Confirm timeout alarms if ACK never changes

---

## Troubleshooting

### PLC sends command but robot does nothing

- Check target routing logic
- Check that `Cmd_Valid` is actually being mapped out
- Check field I/O addressing
- Check robot-side program is reading the correct byte and bit

### ACK never registers

- Verify the ACK input point
- Verify the robot is toggling the correct signal
- Confirm edge logic is comparing current vs previous state
- Confirm the PLC scan is not resetting the bit too quickly

### Command never clears

- Check that ACK edge logic is being evaluated before reset logic
- Check that `Fanuc_Ack_Last` is updated at the end of scan
- Check that no other rung or ST block is rewriting the active state

### Timeout happens too quickly

- Recalculate based on actual PLC task time
- Example: 25 scans only equals 500 ms if the task is truly 20 ms

---

## Expansion Ideas

- Add ABB, UR, and machine cells using the same pattern
- Add a response byte in addition to ACK
- Add command history logging
- Add HMI command labels from a lookup table
- Add retry count and fault escalation
- Add heartbeat loss alarms per cell

---

## Why This Project Matters

This shows practical controls engineering work:

- PLC logic design
- field communication structure
- robot integration
- timeout and fault handling
- scalable architecture for multiple cells

This is the kind of project that reads well in a portfolio because it solves a real integration problem instead of just proving that one device can turn another one on.

---

## Author Notes

This repo is written as a reusable reference for future robot-cell integration work. The examples are intentionally simple and readable so they can be adapted to different PLC brands and robot platforms.

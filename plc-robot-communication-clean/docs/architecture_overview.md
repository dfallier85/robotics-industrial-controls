# Architecture Overview

## Main idea

The PLC and robot should communicate through a small, clearly defined interface.

## Typical roles

### PLC
- owns machine sequence
- issues commands
- watches acknowledgments
- applies timeout / interlock logic
- reports machine-level faults

### Robot
- receives command
- executes robot-side action
- reports acknowledgement
- reports busy / done / fault state

## Good boundary

The PLC should not need robot-native motion syntax.
The robot should not need full machine sequence ownership.

That division keeps the interface much cleaner.

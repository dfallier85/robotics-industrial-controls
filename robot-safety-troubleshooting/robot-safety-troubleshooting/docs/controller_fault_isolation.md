# Controller Fault Isolation

## When to suspect the controller side

Start looking controller-side when:
- field device tests good
- wiring path seems intact
- relay behavior looks correct
- but the robot or PLC still reports the safety path as open

## Possible controller-side problems

- blown fuse in a safety-related path
- failed input circuit
- controller configuration mismatch
- stored fault that requires a different reset path
- startup issue after long power-down
- battery or memory related behavior on older systems

## Good controller-side checks

### 1. Confirm the controller input state
Look at:
- robot I/O screen
- PLC input tag
- HMI diagnostic tag

### 2. Check reset conditions
The controller may need:
- a reset button
- a mode change
- a fault acknowledgment
- another interlock satisfied first

### 3. Check fuses and safety references
If documentation is available:
- identify the relevant fuse
- inspect whether the safety feed is present
- check for loss of supply into a safety board or module

## Important reminder

Do not jump straight to bad controller.
Rule out the field side first.
But once the field side is clean, do not ignore the possibility that the problem is inside the controller or its supporting safety hardware.

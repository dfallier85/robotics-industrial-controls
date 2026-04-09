# Cell Signal Flow Example

## Scenario

A part enters a robotic pick-and-place cell.

## Flow

1. sensor confirms part present
2. PLC marks station ready
3. PLC commands robot or vision inspection step
4. vision optionally returns part validity or position
5. PLC confirms interlocks / permissives
6. PLC issues robot command
7. robot acknowledges and executes motion
8. robot reports busy / done / fault
9. PLC advances machine sequence
10. HMI reflects current machine status

## Why this helps

It shows how signals move through the cell instead of treating it like a black box.

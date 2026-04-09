# Pick-and-Place Cell Example

## Typical components

- robot arm
- gripper / EOAT
- PLC
- HMI
- part-present sensor
- fixture or infeed conveyor
- optional vision system
- safety devices

## Example ownership

### PLC
- manages cycle state
- verifies station ready
- commands robot action

### Robot
- performs pick/place motion
- controls EOAT action
- reports completion

### HMI
- starts, stops, resets
- shows machine state
- shows fault messages

## Why this matters

This is a common and easy-to-explain example of full cell architecture in practice.

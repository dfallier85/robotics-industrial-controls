# PLC Integration Notes

## What the PLC should own

In most industrial systems, the PLC should handle:
- cell readiness
- interlocks
- machine state
- alarm state
- command permissives
- sequence ownership at the machine level

## What the PLC should usually not own

The PLC should usually not need to know:
- robot-native socket syntax
- Node-RED UI details
- MQTT dashboard layout

That keeps the system cleaner.

## Good PLC roles in this architecture

### 1. Publish readiness or interlock status
Example topics:
- `system/plc/interlock`
- `system/plc/status`

### 2. Block or permit commands
The PLC may expose whether:
- doors are closed
- station is ready
- reset is required
- auto mode is active

### 3. Report faults upward
A PLC can publish a message that tells the UI why a robot command should not be sent or should not be executed.

## Important design choice

You can let Node-RED send a command directly to a robot topic, but still use PLC-published interlock status to determine whether the button should be enabled or whether the operator should be warned.

That gives you flexibility without pretending the PLC is optional in a real machine.

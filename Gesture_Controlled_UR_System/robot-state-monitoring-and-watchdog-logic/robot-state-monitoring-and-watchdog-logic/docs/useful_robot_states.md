# Useful Robot States

## Typical useful values

A state-monitoring layer may watch:

- robot mode
- safety mode
- TCP pose
- actual joint positions
- digital inputs
- speed scaling
- runtime / connection status

## Why these are useful

### Robot mode
Tells whether the robot is in an expected operating state.

### Safety mode
Helps detect whether motion should be blocked or stopped.

### TCP pose
Useful for workspace limiting and diagnostics.

### Joint positions
Useful for logging and additional guard logic.

### Digital inputs
Useful for deadman switches, interlocks, or external permissives.

## Practical note

Not every project needs every state value, but the monitoring layer should clearly document which ones matter and why.

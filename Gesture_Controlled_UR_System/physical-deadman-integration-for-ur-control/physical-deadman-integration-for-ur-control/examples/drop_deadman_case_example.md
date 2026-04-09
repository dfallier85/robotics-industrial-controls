# Drop Deadman Case Example

## Scenario

Robot is moving under valid control, then the operator releases the deadman.

## Flow

1. motion is active
2. deadman input changes to false
3. motion permission becomes false
4. dispatcher issues stop
5. active command is cleared or suppressed
6. no new motion is allowed until deadman is held again

## Why this matters

This is the moment where the physical deadman proves it is not just symbolic.

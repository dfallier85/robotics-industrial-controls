# Command Lifecycle Example

## Scenario

The PLC sends a `Home` command to a robot.

## Flow

1. PLC writes command code for `Home`
2. PLC sets command-valid bit
3. Robot sees command and acknowledges it
4. PLC sees ACK and knows the robot received the command
5. Robot executes homing sequence
6. Robot reports busy during execution
7. Robot reports done when finished
8. PLC continues machine sequence

## Why this matters

This is the basic communication loop that makes robot integration predictable.

# Naming and Scaling

## Main point

The communication layer should scale beyond one robot.

## Good tag naming pattern

Examples:
- `UR_Cmd`
- `UR_Cmd_Valid`
- `UR_Ack`
- `UR_Busy`
- `UR_Done`
- `UR_Fault`

For another robot:
- `ABB_Cmd`
- `ABB_Cmd_Valid`
- `ABB_Ack`
- `ABB_Busy`
- `ABB_Done`
- `ABB_Fault`

## Why this matters

Good naming makes it easier to:
- read the logic
- expand to more robots
- debug HMI tags
- explain the interface to others

## Good scaling rule

Use the same interface pattern for each cell where possible.
That consistency is worth a lot.

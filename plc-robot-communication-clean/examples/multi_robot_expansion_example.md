# Multi-Robot Expansion Example

## Scenario

One PLC controls both a UR and an ABB cell.

## Good pattern

Use the same interface shape for each robot:

### UR
- `UR_Cmd`
- `UR_Cmd_Valid`
- `UR_Ack`
- `UR_Busy`
- `UR_Done`
- `UR_Fault`

### ABB
- `ABB_Cmd`
- `ABB_Cmd_Valid`
- `ABB_Ack`
- `ABB_Busy`
- `ABB_Done`
- `ABB_Fault`

## Why this helps

The machine logic stays consistent.
You do not reinvent the interface every time a new robot is added.

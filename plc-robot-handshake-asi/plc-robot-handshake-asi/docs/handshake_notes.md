# Handshake Notes

## Main Design Choice

This design uses an ACK **toggle** instead of waiting for ACK to hold a fixed state.

That means the PLC only cares that the ACK changed since the last scan.

This is useful because:
- the robot does not need to hold ACK high
- the PLC can accept either edge
- the logic scales well across multiple cells

## Recommended Signal Rules

- Keep the command byte separate from status bits
- Reserve a different bit for heartbeat
- Update the saved ACK state after evaluating the edge
- Reset timeout counters when a new command starts
- Document command codes clearly

## Good Documentation Habits

For every cell, keep a sheet that lists:
- command code
- command name
- expected robot action
- ACK behavior
- timeout behavior
- fault response

## Scaling to More Cells

You can repeat the same pattern for:
- UR
- ABB
- Fanuc
- standalone machines

The clean way is to give each target:
- its own command byte
- its own active flag
- its own ACK state tracking
- its own timeout logic

# Stop Behavior

## Main point

When the system decides motion is no longer valid, it should have a defined stop behavior.

## Good triggers for stop

Examples:
- watchdog expired
- bad safety mode
- robot mode changed
- deadman dropped
- communication error
- application shutdown

## Good stop design

A good system should define:
- what stop call is used
- how aggressively it stops
- whether the active command is cleared
- what gets logged

## Why this matters

The difference between:
- “motion ended”
and
- “motion ended in a known, repeatable way”

is a big one.

# Gating Flow Example

## Scenario

The command layer requests motion in +Y.

## Flow

1. resolver requests `move +Y`
2. safety gate checks robot mode
3. safety gate checks safety mode
4. safety gate checks deadman input
5. safety gate checks workspace direction
6. safety gate checks watchdog freshness
7. if all pass, dispatcher sends motion
8. if any fail, command is blocked or reduced

## Why this helps

It makes the permission path visible instead of burying it inside motion code.

# Event Flow Example

## Scenario

Right hand makes a valid POINT gesture.

## Flow

1. camera captures frame
2. hand landmarks detected
3. classifier returns `POINT`
4. resolver maps `POINT` -> `move +Z`
5. safety gate checks:
   - robot mode OK
   - safety mode OK
   - deadman true
   - workspace allows +Z
6. dispatcher sends motion command
7. if gesture disappears or watchdog expires, dispatcher stops motion

## Why this helps

It shows exactly where decisions happen instead of treating the system like magic.

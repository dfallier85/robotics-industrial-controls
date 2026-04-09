# Event Flow Example

## Scenario

Camera detects a gesture that maps to +Y motion.

## Flow

1. camera captures frame
2. vision pipeline returns `THUMBS_UP`
3. resolver maps `THUMBS_UP` -> `move +Y`
4. safety gate checks robot mode, safety mode, deadman, workspace
5. watchdog confirms the intent is fresh
6. dispatcher sends motion to RTDE
7. if the gesture disappears or times out, dispatcher stops motion

## Why this helps

It shows the exact path from visual input to controlled robot motion.

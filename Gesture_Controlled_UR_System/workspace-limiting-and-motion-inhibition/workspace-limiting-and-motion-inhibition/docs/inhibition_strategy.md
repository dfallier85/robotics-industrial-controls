# Inhibition Strategy

## Goal

Suppress only the unsafe motion component instead of killing everything unnecessarily.

## Example idea

If the robot is near `x_max` and the requested command contains `+X`, then:
- block the `+X` component
- allow other safe components such as `+Y` or `-Z`

## Why this is better

This keeps the system usable near the edges of the workspace instead of making it feel broken.

## Typical logic pattern

1. read current pose
2. compare pose to workspace bounds
3. compare requested velocity direction to limit direction
4. zero any component pushing farther into the limit
5. pass through the remaining safe components

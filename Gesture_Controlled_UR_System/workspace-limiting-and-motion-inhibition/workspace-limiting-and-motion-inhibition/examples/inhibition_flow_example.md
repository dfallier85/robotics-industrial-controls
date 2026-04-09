# Inhibition Flow Example

## Scenario

Requested command:
```text
[+X, +Y, 0, 0, 0, 0]
```

Current pose is near `x_max`, but not near `y_max`.

## Flow

1. command layer requests `+X +Y`
2. workspace limiter checks current pose
3. limiter sees `+X` would move farther into `x_max`
4. limiter zeros `+X`
5. limiter keeps `+Y`
6. dispatcher receives:
```text
[0, +Y, 0, 0, 0, 0]
```

## Why this matters

This is a clean example of directional motion inhibition instead of full command rejection.

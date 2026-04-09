# Axis Component Suppression

## Main point

A motion command can contain multiple components at once.

Example:
- `+X`
- `+Y`
- `+Z`
- rotations

If one component is unsafe, you do not always need to discard the entire command.

## Example

Requested velocity:
```text
[+X, +Y, 0, 0, 0, 0]
```

Robot is near `x_max`.

Safe result:
```text
[0, +Y, 0, 0, 0, 0]
```

## Why this matters

This keeps the motion logic more useful and less frustrating.

It also makes the behavior easier to explain:
- “X was blocked, Y was still allowed”

# Workspace Concepts

## Main idea

A workspace limit defines where robot motion is allowed.

Typical limits are expressed as ranges such as:
- x_min / x_max
- y_min / y_max
- z_min / z_max

## Why this matters

In custom motion systems, the command source may not understand physical layout, fixtures, or demo boundaries.

The workspace limiter adds that awareness.

## Good practical interpretation

The limit layer answers:

- where is the robot now?
- which way is it trying to move?
- would that move push farther into a restricted area?

If yes, that component should be suppressed.

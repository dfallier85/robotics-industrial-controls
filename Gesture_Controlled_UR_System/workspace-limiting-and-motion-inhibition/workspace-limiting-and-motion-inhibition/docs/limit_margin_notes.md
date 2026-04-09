# Limit Margin Notes

## Why margins matter

You usually do not want to wait until the robot is exactly at the hard boundary before suppressing motion.

Instead, use a margin zone near the limit.

## Example

If:
- `x_max = 0.60`
- `margin = 0.05`

Then positive X motion might be suppressed once:
- `x >= 0.55`

## Why this helps

It gives the system a buffer and reduces the chance of oscillation or edge-chasing behavior near the boundary.

## Good reminder

Margins are part of system tuning.
They should be documented and explained, not treated as magic numbers.

# Timing and Freshness

## Why timing matters

Vision results can go stale quickly.

Examples:
- gesture disappears
- tracked object moves
- camera drops frames
- pipeline latency rises

## Good design rule

Treat vision-derived commands as valid only for a short freshness window unless they are continuously refreshed.

## Typical support layers

- debounce logic
- command timestamps
- watchdog timeout
- forced stop on stale input

## Why this helps

It prevents the robot from acting on old camera information that is no longer true.

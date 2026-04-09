# Command Suppression

## Main point

A blocked command should not just silently disappear.

The system should know *why* it was suppressed.

## Useful suppression reasons

Examples:
- deadman false
- robot mode not allowed
- safety mode not normal
- watchdog expired
- +X blocked by workspace limit
- +Z blocked near ceiling limit

## Why this matters

When motion does not happen, you want an answer better than:
- “it just didn’t move”

Suppression reasons make the system much easier to test and trust.

## Useful behaviors

A safety gate may:
- block the whole command
- zero one component of velocity
- allow only safe axes
- force stop if all motion becomes invalid

# Motion Permission Logic

## Main idea

The deadman should be one of the required conditions for motion permission.

## Example rule

Motion allowed only if:
- robot mode is acceptable
- safety mode is acceptable
- deadman input is active
- watchdog is fresh
- workspace limiter allows the direction

## Why this matters

This keeps motion permission explicit.

The system should be able to say:
- allowed because deadman is active
- blocked because deadman is false

That is much easier to trust and debug.

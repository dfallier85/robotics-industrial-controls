# Safety and State Interaction

## Main point

Vision input does not override robot safety and state checks.

The motion layer should still verify:
- robot mode
- safety mode
- deadman state
- workspace limits
- command freshness

## Why this matters

A camera may produce a valid-looking result while the robot is not in a valid motion state.

The system should be able to say:
- “vision result valid”
- but also
- “motion still blocked”

That is a stronger and clearer design.

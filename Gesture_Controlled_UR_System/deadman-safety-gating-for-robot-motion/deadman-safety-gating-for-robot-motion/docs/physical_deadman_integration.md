# Physical Deadman Integration

## Main point

A physical deadman input is often the stronger and more realistic approach for real robot-control systems.

## Typical pattern

A physical device is wired to:
- robot digital input
- PLC input
- or another approved enable path

Then the motion code reads that state indirectly through the system's normal interfaces.

## Why this matters

A physical deadman is harder to fake accidentally and better matches real enabling-device expectations.

## Good design practice

Document:
- where the deadman signal comes from
- what input it maps to
- what state means motion allowed
- what state means motion blocked
- what happens when the signal drops during active motion

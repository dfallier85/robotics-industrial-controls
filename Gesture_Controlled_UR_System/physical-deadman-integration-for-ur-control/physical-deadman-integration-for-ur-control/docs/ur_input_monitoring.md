# UR Input Monitoring

## Main point

The control loop needs a reliable way to read the relevant input state.

## Typical values to monitor

Examples:
- digital input state
- robot mode
- safety mode

## Why this matters

A physical deadman by itself is not useful unless the control loop actually checks it before allowing motion.

## Good logic pattern

Before sending motion:
- read robot mode
- read safety mode
- read deadman input
- allow motion only if all expected conditions are true

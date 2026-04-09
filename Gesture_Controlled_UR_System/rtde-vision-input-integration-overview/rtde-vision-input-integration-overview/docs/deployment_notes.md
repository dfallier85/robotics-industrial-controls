# Deployment Notes

## Things to document

- camera type and placement
- host device
- robot IP
- RTDE package / runtime path
- model or perception method used
- confidence thresholds
- timing assumptions
- safety gating strategy
- watchdog timeout

## Why this matters

A system like this depends on more than code.

It depends on:
- environment
- camera geometry
- runtime configuration
- robot state assumptions
- how vision output is interpreted

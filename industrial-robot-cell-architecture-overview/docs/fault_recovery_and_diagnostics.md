# Fault Recovery and Diagnostics

## Why this matters

A good cell architecture explains not only how the machine runs, but also how it fails and recovers.

## Typical recovery questions

- what happens when the robot faults?
- what happens when vision fails?
- what happens when a safety path opens?
- what happens when a command times out?
- how does the operator recover?
- how does the PLC know the cell is ready again?

## Good design goal

Fault handling should be:
- explicit
- diagnosable
- recoverable
- documented

That makes maintenance and troubleshooting much stronger.

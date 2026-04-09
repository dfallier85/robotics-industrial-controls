# Deadman Role

## Main idea

A physical deadman is a held enable signal that must remain active for motion to remain allowed.

If the operator releases it:
- motion should stop
- new motion should not be issued
- the system should return to a safe non-motion state

## Why this matters

This is stronger than:
- a one-time button press
- a stale software flag
- motion that continues after the user stops intending it

## Practical meaning

The deadman says:
- "the human is actively permitting motion right now"

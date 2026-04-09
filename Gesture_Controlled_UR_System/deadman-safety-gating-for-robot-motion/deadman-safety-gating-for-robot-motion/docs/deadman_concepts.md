# Deadman Concepts

## Main idea

A deadman condition is an explicit enable signal that must stay true for motion to remain allowed.

If the deadman is released:
- motion should stop
- new motion should not be issued
- the system should fall back to a safe idle state

## Why this matters

It prevents motion from continuing just because an old command is still present.

In practical terms, the deadman says:
- “yes, the human still intends motion right now”

## Common forms

- physical switch
- pendant-style enable
- external safety handle
- software-held enable state in tightly limited lab demos

## Good rule

Use physical deadman hardware when the real system calls for it.

Software-only deadman logic may be useful for prototyping, but it is not the same thing as a dedicated physical enable device.

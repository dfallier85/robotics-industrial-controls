# Watchdog Flow Example

## Scenario

A valid motion command is being refreshed normally, then the command source stops updating.

## Flow

1. command source provides valid motion
2. timestamp is refreshed each loop
3. watchdog sees command age within limit
4. motion remains allowed
5. command source stops updating
6. command age exceeds timeout
7. watchdog declares command stale
8. dispatcher sends stop
9. active command is cleared

## Why this helps

It shows exactly how the system transitions from valid motion to forced stop.

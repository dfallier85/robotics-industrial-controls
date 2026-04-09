# Status and Faults

## Why this matters

A command interface is incomplete if the PLC cannot tell what happened after the command.

## Useful robot-to-PLC signals

- `Busy`
- `Done`
- `Fault`
- optional `StatusWord`
- optional `ActiveCommandEcho`

## Good use

### Busy
Robot is executing work or not yet ready for another command.

### Done
Robot completed the requested action.

### Fault
Robot could not complete the action or needs intervention.

## Good design rule

Do not make the PLC guess whether a command succeeded.
Give it explicit status feedback.

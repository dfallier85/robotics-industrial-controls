# Interaction with Safety Gate

## Main point

Workspace limiting is not a replacement for the safety gate.

Both layers have roles.

## Good separation

### Safety gate
Checks:
- robot mode
- safety mode
- deadman
- watchdog
- high-level motion permission

### Workspace limiter
Checks:
- current position
- requested direction
- bounds and margins
- axis-specific inhibition

## Why this separation helps

The safety gate decides whether motion is allowed at all.

The workspace limiter decides whether specific motion components are allowed at the current position.

That keeps the control system clearer.

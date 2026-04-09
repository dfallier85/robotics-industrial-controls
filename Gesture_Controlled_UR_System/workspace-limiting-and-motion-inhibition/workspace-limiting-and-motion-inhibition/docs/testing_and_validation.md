# Testing and Validation

## Goal

Verify the workspace limiter behaves as expected at normal positions and near each boundary.

## Good checks

- motion fully allowed in center region
- `+X` blocked near `x_max`
- `-X` blocked near `x_min`
- `+Y` blocked near `y_max`
- `-Y` blocked near `y_min`
- `+Z` blocked near `z_max`
- `-Z` blocked near `z_min`

## Mixed-command checks

Also test commands with multiple components:
- `+X +Y`
- `+Y +Z`
- `-X -Z`

Confirm that:
- only unsafe components are removed
- safe components still pass through

## Good habit

Document:
- pose used for test
- requested motion
- allowed output
- whether the result matched expectation

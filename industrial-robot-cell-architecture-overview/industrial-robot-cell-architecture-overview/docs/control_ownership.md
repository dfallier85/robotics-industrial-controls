# Control Ownership

## Main point

A cell becomes easier to understand when ownership is explicit.

## Good ownership split

### PLC owns
- machine sequence
- interlocks
- command timing
- station readiness
- machine-level faults
- startup/reset flow

### Robot owns
- motion execution
- path logic
- robot-side task completion
- robot-specific motion faults

### HMI owns
- operator commands
- display of status / faults
- guided recovery prompts

### Vision owns
- result generation from images
- positional or inspection output

## Why this matters

The PLC should not need to own every robot path detail.
The robot should not need to own full machine sequencing.

That separation is a major part of clean cell architecture.

# System Architecture

## Basic Flow

```text
[Camera]
   ->
[Hand / Gesture Perception]
   ->
[Gesture Classification]
   ->
[Command Resolver]
   ->
[Safety Gate]
   ->
[Motion Dispatcher]
   ->
[UR Robot]
```

## Why this split matters

A strong system avoids mixing everything into one script.

That lets you reason about:
- what the model sees
- what the command layer believes
- what the safety layer allows
- what the robot actually receives

## Good module boundaries

- perception module
- resolver module
- safety module
- dispatcher module
- config module
- main loop / orchestration

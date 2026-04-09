# Module Boundary Example

## Suggested file roles

- `perception.py` -> camera input and vision result
- `resolver.py` -> result-to-intent mapping
- `safety_gate.py` -> permission checks
- `dispatcher.py` -> RTDE motion commands
- `settings.py` -> config values
- `main.py` -> orchestration loop

## Why this helps

Each layer has one main job.
That keeps the system much easier to maintain and explain.

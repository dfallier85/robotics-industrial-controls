# Module Split Example

## Suggested file roles

- `main.py` -> orchestration loop
- `perception.py` -> hand detection / gesture classification
- `resolver.py` -> gesture-to-command mapping
- `safety_gate.py` -> state and workspace checks
- `dispatcher.py` -> RTDE motion commands
- `settings.py` -> config values

## Why this helps

Each module has a clear job.
That makes debugging and explanation much easier.

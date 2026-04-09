# Loop Health and Freshness

## Freshness

A command is fresh only if it was updated recently enough.

Example:
- watchdog timeout = 0.30 s
- last valid command older than 0.30 s
- command becomes stale

## Loop health

The control loop should also care whether the application itself is still running correctly.

Examples of bad loop health:
- camera froze
- main loop blocked
- no new gesture result
- RTDE receive failed
- exception occurred upstream

## Why this matters

A healthy system needs both:
- fresh command data
- healthy loop behavior

That is safer than trusting motion just because one old command existed.

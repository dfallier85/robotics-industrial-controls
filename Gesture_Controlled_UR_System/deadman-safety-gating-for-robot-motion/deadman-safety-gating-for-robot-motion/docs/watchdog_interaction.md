# Watchdog Interaction

## Why this matters

Deadman logic alone is not enough.

If the control loop dies, the robot should not keep coasting on stale intent.

## Basic idea

The watchdog ensures that motion commands remain fresh.

If fresh commands stop arriving within a short timeout:
- stop motion
- clear active command
- require fresh enable conditions again

## Combined rule

Good systems often require both:
- deadman active
- watchdog fresh

That means motion needs both:
- human intent
- healthy control loop behavior

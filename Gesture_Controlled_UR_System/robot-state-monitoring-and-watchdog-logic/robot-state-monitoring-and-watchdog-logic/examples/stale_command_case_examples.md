# Stale Command Case Examples

## Case 1: Gesture source disappears

- Last command: `+Y`
- No new gesture data arrives
- Timeout exceeded

Result:
- stop motion
- clear command
- log stale command reason

---

## Case 2: Loop crash during motion

- Loop previously commanding motion
- Exception stops refresh cycle
- Watchdog timer expires

Result:
- robot motion should be stopped by the cleanup / watchdog path

---

## Case 3: Safety mode changes during active motion

- Motion command still fresh
- Safety mode becomes invalid

Result:
- suppress motion or stop immediately
- reason should reference safety state, not just timeout

# Timeout and Retry

## Main idea

A command should not wait forever for acknowledgment or completion.

## Common timeout uses

- ACK timeout
- command completion timeout
- communication loss timeout

## Why this matters

Timeouts help separate:
- real success
- stalled communication
- robot fault
- machine sequencing issue

## Retry thinking

Retries can be useful, but only if:
- the action is safe to repeat
- duplicate execution will not cause damage
- the retry count is limited
- the event is logged or diagnosable

## Good default

For many systems:
- detect timeout
- raise clear fault
- require operator or sequence-level recovery

That is often safer than blind retries.

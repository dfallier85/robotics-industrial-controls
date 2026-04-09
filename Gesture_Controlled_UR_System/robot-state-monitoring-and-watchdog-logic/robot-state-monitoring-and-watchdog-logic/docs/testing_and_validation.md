# Testing and Validation

## Goal

Verify that state monitoring and watchdog behavior work correctly in both normal and failure conditions.

## Good checks

- fresh command allows motion
- stale command triggers stop
- dropping command updates triggers stop
- bad safety mode suppresses motion
- robot mode change suppresses motion
- shutdown path stops cleanly
- suppression / stop reason is logged or identifiable

## What to document

Write down:
- test condition
- expected result
- actual result
- timeout used
- stop behavior observed

## Good habit

Test failure and timeout cases on purpose.
That is how you prove the watchdog is real and not just a variable in a file.

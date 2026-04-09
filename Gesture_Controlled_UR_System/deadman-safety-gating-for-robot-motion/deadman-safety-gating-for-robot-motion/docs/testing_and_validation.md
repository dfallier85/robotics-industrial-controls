# Testing and Validation

## Goal

Verify the gating logic behaves correctly in both allowed and blocked conditions.

## Good checks

- deadman true allows motion
- deadman false blocks motion
- dropping deadman during motion stops robot
- bad robot mode blocks motion
- bad safety mode blocks motion
- workspace limit blocks unsafe direction
- watchdog expiry stops motion

## What to document

Write down:
- what condition was tested
- expected result
- observed result
- whether motion stopped cleanly
- whether suppression reason was correct

## Good habit

Test blocked states on purpose, not just success states.
That is how you prove the safety gating actually does something.

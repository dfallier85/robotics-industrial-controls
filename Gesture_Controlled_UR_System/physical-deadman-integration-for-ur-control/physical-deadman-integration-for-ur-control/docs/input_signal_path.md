# Input Signal Path

## Goal

Understand where the deadman signal actually enters the system.

## Typical path

```text
[Physical Deadman Device]
        ->
[Wired Input]
        ->
[Robot or Control Input State]
        ->
[Python / RTDE Monitoring Layer]
        ->
[Motion Permission]
```

## Why this matters

The signal path should be documented clearly.

You want to know:
- what hardware generates the signal
- what input receives it
- what state means enabled
- how that state is read by the control code

## Good rule

Never leave input meaning vague.
Write down:
- signal source
- input number or mapping
- active state
- blocked state

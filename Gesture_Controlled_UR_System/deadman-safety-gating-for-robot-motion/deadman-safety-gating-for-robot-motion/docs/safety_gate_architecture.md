# Safety Gate Architecture

## Goal

Put a clear permission layer between command intent and robot motion.

## Basic structure

```text
[Resolver / UI / Perception]
           ->
      [Safety Gate]
           ->
    [Motion Dispatcher]
           ->
        [Robot]
```

## What the safety gate checks

Typical checks include:
- robot mode allowed
- safety mode allowed
- deadman active
- workspace direction allowed
- watchdog still fresh

## Why this works

It keeps motion approval in one place.

That means:
- easier debugging
- easier documentation
- easier expansion
- less chance that unsafe logic is hidden across multiple files

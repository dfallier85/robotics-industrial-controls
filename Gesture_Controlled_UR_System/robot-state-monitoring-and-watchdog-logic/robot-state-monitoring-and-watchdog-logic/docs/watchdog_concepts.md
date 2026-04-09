# Watchdog Concepts

## Main idea

A watchdog prevents motion from continuing when the control loop stops refreshing valid commands.

## Basic rule

If a valid command is not refreshed within a short time window:
- stop motion
- clear active command
- require fresh approval before moving again

## Why this matters

Without a watchdog:
- loop crash may leave motion behavior unclear
- stale commands may persist too long
- operator intent may be lost while motion logic still thinks it is active

## Good design goal

The watchdog should be boring, predictable, and easy to explain.

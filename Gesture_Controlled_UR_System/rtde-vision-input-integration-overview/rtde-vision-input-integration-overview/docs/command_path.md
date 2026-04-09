# Command Path

## Goal

Turn vision-derived intent into a controlled path toward motion.

## Example path

1. vision result arrives
2. intent resolver maps result to a command
3. command passes through safety gate
4. watchdog / freshness checks confirm the command is still current
5. dispatcher sends approved motion
6. dispatcher stops motion when intent disappears or becomes invalid

## Why this matters

This keeps the robot from reacting directly to every flicker or unstable vision output.

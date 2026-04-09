# Watchdog and Shutdown

## Why this matters

A gesture-controlled robot needs defined behavior when:
- the loop dies
- tracking is lost
- communication fails
- the user quits
- the camera freezes

## Good behavior

A strong design includes:
- motion stop on shutdown
- watchdog timeout for stale commands
- clear cleanup path
- no “robot keeps drifting because the loop stopped”

## Example idea

If no valid motion command is refreshed within a short watchdog window:
- issue stop
- clear last command
- log the reason

That makes failures much safer and easier to understand.

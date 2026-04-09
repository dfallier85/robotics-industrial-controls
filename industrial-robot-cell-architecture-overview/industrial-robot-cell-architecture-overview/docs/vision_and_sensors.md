# Vision and Sensors

## Main idea

Vision and sensors provide the cell with information about the world outside the PLC scan table.

## Common inputs

- part present / absent
- location / offset
- pass / fail inspection
- object identity
- conveyor / station sensors
- EOAT confirmation signals

## Typical role in cell architecture

These systems feed:
- the PLC
- the robot
- or both

The architecture should explain:
- what they detect
- how their results are used
- what happens when they fail or time out

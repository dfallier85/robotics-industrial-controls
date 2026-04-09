# Command Resolution

## Main idea

The resolver turns gestures into robot-intent commands.

That means:
- not every gesture becomes motion
- conflicting gestures need a rule
- some gestures may be reserved for stop or special behavior

## Example mapping idea

Examples:
- POINT -> +Z
- PEACE -> -Z
- THREE -> +X
- FOUR -> -X
- THUMBS_UP -> +Y
- FIST -> -Y

## Why this layer matters

This is where you define meaning.

The classifier says:
- “gesture = POINT”

The resolver says:
- “POINT means move robot +Z”

That is a very important separation.

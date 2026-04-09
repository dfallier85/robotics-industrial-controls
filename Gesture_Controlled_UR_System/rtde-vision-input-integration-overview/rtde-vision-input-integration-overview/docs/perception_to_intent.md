# Perception to Intent

## Main idea

Vision should usually produce an intermediate result, not direct robot motion.

Examples:
- gesture = POINT
- object center inside ROI
- target offset = +X
- object class = bottle

Then another layer translates that into command intent.

## Why this matters

This separates:
- what the camera observed
from
- what the robot should do about it

That is a very important design boundary.

## Good future patterns

- thresholding weak perception
- debounce logic
- confidence gating
- temporal smoothing

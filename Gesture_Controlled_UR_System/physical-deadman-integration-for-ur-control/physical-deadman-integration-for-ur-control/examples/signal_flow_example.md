# Signal Flow Example

## Scenario

Operator holds the physical deadman and requests motion.

## Flow

1. operator holds deadman
2. input goes true
3. control loop reads input as active
4. other gating conditions are checked
5. motion is allowed
6. dispatcher sends motion to the robot

## Why this helps

It shows that motion permission is tied to a live physical condition, not only a software request.

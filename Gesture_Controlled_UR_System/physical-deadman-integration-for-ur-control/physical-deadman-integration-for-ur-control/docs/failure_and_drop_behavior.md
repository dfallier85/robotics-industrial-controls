# Failure and Drop Behavior

## Main point

The deadman is most important when it goes false during active motion.

## Expected behavior

If the deadman drops:
- motion should stop
- active command should be cleared or suppressed
- fresh motion should require deadman active again

## Other failure cases

Also consider:
- input signal lost
- wrong input mapping
- noisy / unstable input state
- robot state changes while deadman remains held

## Good design goal

The system should fail in a way that is clear and explainable, not mysterious.

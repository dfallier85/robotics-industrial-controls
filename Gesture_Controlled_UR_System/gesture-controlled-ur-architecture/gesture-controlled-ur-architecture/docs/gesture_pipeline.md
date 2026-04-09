# Gesture Pipeline

## Goal

Turn camera input into a stable gesture signal.

## Typical stages

1. capture frame
2. detect hand(s)
3. track landmarks
4. classify gesture
5. output gesture label + confidence

## Why this matters

The robot should not react directly to raw hand pixels.

You want a cleaner intermediate result such as:
- right hand = POINT
- left hand = OPEN_PALM
- confidence above threshold

## Good future upgrades

- confidence thresholds
- per-hand thresholds
- temporal smoothing
- debounce windows
- two-hand conflict handling

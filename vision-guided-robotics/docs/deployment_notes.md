# Deployment Notes

## 1. Camera Placement

Document:
- height
- angle
- field of view
- distance to target
- whether the robot or part is moving during capture

## 2. Lighting Setup

Document:
- light type
- position
- intensity
- whether ambient light affects the image

## 3. Part Presentation

Ask:
- is the part always in the same place?
- can it rotate?
- can it tilt?
- is there glare?
- can background clutter confuse the image?

## 4. Coordinate Frames

For position-guided systems, define:
- camera frame
- part frame
- robot frame
- any offset or calibration relationship

## 5. Timing

Document:
- trigger-to-result time
- allowed robot wait time
- cycle time impact
- what timeout threshold is acceptable

## 6. Failure Modes

Define behavior for:
- no part found
- inspection fail
- low-confidence or unstable result
- communication timeout
- robot motion failure
- operator reset

## 7. Maintenance Considerations

A VGR system should be maintainable by someone other than the original builder.

Document:
- how to reteach
- how to check lighting
- how to verify focus
- how to test I/O
- how to recover after power cycle

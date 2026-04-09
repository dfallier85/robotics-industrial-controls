# Integration Workflow

## Goal

Turn an image result into a repeatable machine action.

## Typical Workflow

### 1. Present the part
A part arrives in the field of view by fixture, tray, conveyor, or robot placement.

### 2. Trigger image acquisition
The system triggers the camera or vision controller.

Trigger sources may include:
- PLC output
- robot digital output
- internal vision trigger
- encoder / sensor event

### 3. Process the image
The vision controller evaluates the programmed tools.

Examples:
- edge detection
- pattern match
- color / contrast decision
- measurement
- blob analysis
- OCR or code read

### 4. Produce a result
Typical result types:
- pass/fail
- part present / absent
- X/Y/rotation offset
- numeric measurement
- class or recipe ID

### 5. Transfer the result
The result is sent to:
- PLC
- robot
- both

### 6. Decide the next action
The control system decides whether to:
- pick
- reject
- sort
- stop the cycle
- request operator intervention
- retry image capture

### 7. Confirm completion
The robot and controller exchange completion or acknowledgment signals so the sequence can continue.

## Key Point

Vision is only one part of the cycle.

A VGR system is successful when the whole chain works:
- part presentation
- image quality
- result quality
- communication quality
- robot action quality

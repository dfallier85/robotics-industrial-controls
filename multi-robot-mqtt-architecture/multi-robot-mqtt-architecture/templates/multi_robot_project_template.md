# Multi-Robot Project Template

## Title
-

## Goal
What is the system trying to accomplish?

## Robots
- UR:
- ABB:
- Other:

## Supervisory Layer
- Node-RED:
- MQTT Broker:
- Bridge device:

## PLC Involvement
What does the PLC own?
- interlocks
- sequence
- readiness
- faults
- other:

## Topic Map
- robot/ur/cmd
- robot/ur/response
- robot/abb/cmd
- robot/abb/response
- system/plc/status
- system/plc/interlock
- system/plc/fault

## Command Examples
- wave
- home
- stop
- reset

## Response Strategy
How are responses formatted?
- plain string
- JSON

## Failure Handling
What happens if:
- broker offline
- bridge offline
- robot offline
- interlock false
- timeout

## Deployment Notes
- IPs
- ports
- network layout
- startup sequence
- recovery steps

## Future Improvements
-

# Pass/Fail Pick Sequence Example

## Scenario

A camera inspects a presented part.  
If the part passes inspection, the robot picks it and places it in the good bin.  
If the part fails inspection, the robot moves it to the reject bin or leaves it for operator handling.

## Sequence

1. Part arrives in inspection position
2. PLC confirms station ready
3. PLC triggers vision inspection
4. Vision sets `Busy`
5. Vision completes inspection
6. Vision returns one of:
   - Pass
   - Fail
   - No Part
7. PLC interprets result
8. PLC commands robot action
9. Robot completes move
10. PLC marks cycle complete

## Possible Robot Actions

### Pass
- pick part
- place in good location
- confirm done

### Fail
- pick and reject
- or hold station and request operator action

### No Part
- raise alarm
- retry
- stop cycle based on machine design

## Important Reminder

The inspection result is only useful if the downstream action is clearly defined.

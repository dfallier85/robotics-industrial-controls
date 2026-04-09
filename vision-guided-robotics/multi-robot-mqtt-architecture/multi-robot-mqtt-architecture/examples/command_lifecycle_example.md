# Command Lifecycle Example

## Scenario

Operator presses a `wave` button for the UR robot.

## Lifecycle

1. Node-RED publishes `wave` to `robot/ur/cmd`
2. UR bridge receives the message
3. UR bridge checks local logic or interlock state if needed
4. UR bridge sends native command to UR robot
5. UR robot responds
6. UR bridge publishes result to `robot/ur/response`
7. Node-RED displays response to operator

## Extended case with PLC interlock

1. PLC publishes `interlock false`
2. Node-RED shows blocked state
3. Operator attempts command anyway
4. Bridge or supervisory logic returns:
   - `result: error`
   - `reason: PLC interlock false`

That makes the failure understandable instead of mysterious.

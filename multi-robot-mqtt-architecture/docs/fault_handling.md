# Fault Handling

## Failure cases to plan for

A multi-robot system needs defined behavior for:
- robot not reachable
- MQTT broker offline
- bridge offline
- command timeout
- PLC interlock false
- robot fault response
- wrong topic or malformed payload

## Recommended responses

### Robot not reachable
Bridge publishes an error on the robot's response topic.

### Bridge offline
Node-RED should show no recent response or a connection-loss indicator.

### PLC interlock false
Node-RED should display the interlock state and block or warn before command issue.

### Command timeout
Use a timeout rule in the bridge or supervisory layer and publish a clear error response.

## Good response format

For richer systems, use structured responses like:

```json
{
  "requested_command": "wave",
  "result": "error",
  "reason": "PLC interlock false"
}
```

That is more useful than just returning `failed`.

## Debugging advice

When something breaks, work from the top down:
1. did Node-RED publish?
2. did the broker receive it?
3. did the correct bridge subscribe?
4. did the bridge attempt the robot command?
5. did the robot reply?
6. did the response return to the expected topic?

# Topic Strategy

## Goal

Make the topic tree easy to understand, easy to debug, and easy to expand.

## Recommended Pattern

### Robot command topics
- `robot/ur/cmd`
- `robot/abb/cmd`

### Robot response topics
- `robot/ur/response`
- `robot/abb/response`

### PLC topics
- `system/plc/status`
- `system/plc/fault`
- `system/plc/interlock`

### Optional global topics
- `system/all/status`
- `system/all/fault`

## Why this works

It gives each subsystem:
- a clear command inlet
- a clear response outlet

That matters when troubleshooting:
- wrong topic
- no subscriber
- bridge offline
- robot replied but UI not listening
- PLC blocked the command

## Things to avoid

- one giant mixed topic for everything
- vague names like `robot/data`
- sending commands and responses on the same topic
- embedding too much logic in topic names

## Suggested payload style

For simple systems:
- plain strings are fine, such as `wave` or `home`

For richer systems:
- JSON payloads are better

Example:
```json
{
  "command": "home",
  "source": "nodered",
  "timestamp": "2026-04-06T12:00:00"
}
```

Use JSON once the system starts needing:
- metadata
- IDs
- status codes
- richer responses

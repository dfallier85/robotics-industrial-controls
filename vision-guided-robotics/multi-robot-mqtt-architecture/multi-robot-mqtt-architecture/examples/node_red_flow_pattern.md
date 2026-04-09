# Node-RED Flow Pattern

## Basic pattern

```text
[Button: UR Wave] -> [MQTT Out: robot/ur/cmd]
[Button: ABB Home] -> [MQTT Out: robot/abb/cmd]

[MQTT In: robot/ur/response] -> [UI / Debug]
[MQTT In: robot/abb/response] -> [UI / Debug]

[MQTT In: system/plc/interlock] -> [UI status / Button enable logic]
[MQTT In: system/plc/fault] -> [Alarm display]
```

## Goal

Keep the flow readable:
- command generation on one side
- response handling on the other
- PLC state visible in a separate lane

That makes maintenance easier.

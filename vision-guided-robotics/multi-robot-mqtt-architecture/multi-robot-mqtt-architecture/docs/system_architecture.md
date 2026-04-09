# System Architecture

## Basic Multi-Robot Flow

```text
[Operator UI / Node-RED]
          ->
      [MQTT Broker]
      /      |      \
     /       |       \
    v        v        v
[UR Bridge][ABB Bridge][PLC Interface]
    |        |         |
    v        v         v
 [UR]      [ABB]    [PLC]
```

## Role of Each Layer

### Node-RED
- operator-facing controls
- dashboard buttons
- status display
- alarm display
- manual testing / demo interface

### MQTT Broker
- message transport hub
- decouples publishers from subscribers
- makes the architecture expandable

### Python Bridges
- subscribe to robot-specific command topics
- translate MQTT commands into robot-native communication
- publish responses back to robot-specific response topics

### PLC
- sequence control
- interlocks
- readiness states
- safety-adjacent machine coordination
- alarm publishing if desired

### Robots
- execute the requested action
- report response or completion state

## Key Point

The biggest benefit of this architecture is separation.

You do not want:
- UI details mixed into robot code
- robot-specific command syntax mixed into the PLC
- PLC interlock logic buried inside Node-RED

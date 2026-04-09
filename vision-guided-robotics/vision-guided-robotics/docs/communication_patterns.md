# Communication Patterns

## Common Ways Vision Talks to the Rest of the Cell

### 1. Discrete I/O
Simple and common.

Examples:
- trigger inspect
- busy
- done
- pass
- fail
- no part found

Best for:
- simple inspection results
- easy troubleshooting
- basic pass/fail systems

### 2. PLC-mediated data exchange
The vision controller sends results to the PLC, then the PLC coordinates the robot.

Best for:
- cells with complex sequence logic
- multiple stations
- centralized interlocks

### 3. Direct robot communication
The vision system sends results directly to the robot controller.

Best for:
- tight robot-vision coupling
- coordinate guidance
- lower-latency direct action

### 4. Networked message-based approach
Examples:
- Ethernet/IP
- Profinet
- TCP socket
- fieldbus-specific data blocks

Best for:
- richer result data
- positional values
- larger systems with structured communication

## What to Document

For every integration, define:
- who sends the trigger
- who owns the result
- what signals mean ready / busy / done
- what timeout looks like
- what happens on no result
- what happens on communication loss

## Practical Advice

Keep the handshake boring and clear.

Fancy communication does not help if nobody can troubleshoot it at 2 AM.

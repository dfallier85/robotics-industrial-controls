# Communications and Networking

## Common communication paths

Industrial robot cells often include communication between:
- PLC and robot
- PLC and HMI
- PLC and vision system
- PLC and remote I/O
- robot and vision system
- supervisory devices and gateways

## Typical patterns

- command / ack handshakes
- status bits
- fault bits
- data words or bytes
- Ethernet/IP, Profinet, Modbus, AS-i, sockets, or similar transport layers

## Why this matters

The architecture should explain:
- what data is exchanged
- who publishes it
- who consumes it
- how failures are detected

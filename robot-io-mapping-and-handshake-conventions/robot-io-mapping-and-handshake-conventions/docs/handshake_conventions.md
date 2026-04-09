# Handshake Conventions

## Typical handshake signals

- Cmd_Valid
- Ack
- Busy
- Done

## Flow

1. PLC sets command
2. PLC sets valid
3. Robot sets ACK
4. PLC clears valid
5. Robot executes

## Why this matters

Consistency across robots reduces engineering time.

# Command Handshake

## Goal

Make command transfer obvious and reliable.

## Simple pattern

Typical elements:
- `Cmd_Code`
- `Cmd_Valid`
- `Ack`
- optional `Busy`
- optional `Done`

## Example sequence

1. PLC writes command code
2. PLC sets command valid
3. Robot sees command and toggles or sets ACK
4. PLC sees ACK and clears active command state
5. Robot performs action
6. Robot optionally sets done / busy / fault bits

## Why this works

It gives both sides a clear contract:
- PLC knows command was seen
- robot knows command was intentionally issued
- both sides can detect when the sequence stalls

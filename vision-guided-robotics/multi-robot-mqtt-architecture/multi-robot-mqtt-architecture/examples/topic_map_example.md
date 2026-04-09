# Topic Map Example

## Robot Topics

| Topic | Purpose |
|---|---|
| `robot/ur/cmd` | Send command to UR bridge |
| `robot/ur/response` | Receive UR response |
| `robot/abb/cmd` | Send command to ABB bridge |
| `robot/abb/response` | Receive ABB response |

## PLC Topics

| Topic | Purpose |
|---|---|
| `system/plc/status` | General PLC machine status |
| `system/plc/interlock` | Interlock or permissive state |
| `system/plc/fault` | Fault / alarm message |

## Example commands

- `wave`
- `home`
- `stop`
- `reset`

## Example idea

A Node-RED page could have:
- UR section
- ABB section
- PLC status section
- combined alarm banner

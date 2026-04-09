# Tag Map Example

## PLC → Robot

| Tag | Type | Purpose |
|---|---|---|
| `UR_Cmd` | `USINT` | Command code for UR |
| `UR_Cmd_Valid` | `BOOL` | Marks command active |
| `ABB_Cmd` | `USINT` | Command code for ABB |
| `ABB_Cmd_Valid` | `BOOL` | Marks command active |

## Robot → PLC

| Tag | Type | Purpose |
|---|---|---|
| `UR_Ack` | `BOOL` | UR acknowledged command |
| `UR_Busy` | `BOOL` | UR busy |
| `UR_Done` | `BOOL` | UR done |
| `UR_Fault` | `BOOL` | UR fault |
| `ABB_Ack` | `BOOL` | ABB acknowledged command |
| `ABB_Busy` | `BOOL` | ABB busy |
| `ABB_Done` | `BOOL` | ABB done |
| `ABB_Fault` | `BOOL` | ABB fault |

## Notes

This pattern keeps each robot interface readable and consistent.

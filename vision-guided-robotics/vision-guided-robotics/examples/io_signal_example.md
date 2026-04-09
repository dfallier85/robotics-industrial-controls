# I/O Signal Example

This is a simple example of discrete signal flow for a vision-guided robot cell.

## Vision Trigger / Result Signals

| Signal Name | Direction | Meaning |
|---|---|---|
| `Vision_Trigger` | PLC -> Vision | Start image capture / inspection |
| `Vision_Busy` | Vision -> PLC | Vision system is processing |
| `Vision_Done` | Vision -> PLC | Result is ready |
| `Vision_Pass` | Vision -> PLC | Inspection passed |
| `Vision_Fail` | Vision -> PLC | Inspection failed |
| `Vision_NoPart` | Vision -> PLC | No valid part found |

## Robot Coordination Signals

| Signal Name | Direction | Meaning |
|---|---|---|
| `Robot_StartAction` | PLC -> Robot | Execute action based on vision result |
| `Robot_Busy` | Robot -> PLC | Robot is in motion / handling action |
| `Robot_Done` | Robot -> PLC | Robot completed action |
| `Robot_Fault` | Robot -> PLC | Robot could not complete commanded action |

## Notes

For more advanced systems, pass/fail may be replaced or supplemented by:
- part ID
- recipe number
- X/Y offset
- angle offset
- measurement result

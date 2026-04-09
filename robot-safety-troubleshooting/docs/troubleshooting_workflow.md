# Troubleshooting Workflow

## Goal

Find the real cause of a robot safety fault without making assumptions too early.

## Step 1: Define the symptom clearly

Start with facts:
- What exact message is shown?
- Where is it shown? Pendant, HMI, PLC alarm list?
- Is the fault steady or flashing?
- Did the issue begin after shutdown, maintenance, or power loss?

Write the exact wording down.

## Step 2: Check the physical input first

Examples:
- magnetic door switch
- tongue interlock
- E-stop mushroom
- reset pushbutton

Use continuity or voltage checks to prove whether the device itself changes state.

A good sensor does not prove the whole circuit is good.
It only proves the sensor is good.

## Step 3: Follow the signal path

Trace the path:
1. device
2. terminal block
3. relay or safety module input
4. relay or safety module output
5. controller input
6. PLC / HMI status bit

At each point, ask:
- what should I see here?
- what do I actually see here?

## Step 4: Separate hardware from logic

If the signal never reaches the controller:
- focus on wiring, terminals, relays, and safety hardware

If the signal reaches the controller but the system still will not recover:
- focus on sequence conditions, reset logic, latched faults, and controller state

## Step 5: Test reset behavior

Check:
- is reset reaching the PLC?
- is the PLC holding reset long enough?
- is another permissive missing?
- is the station stuck at a sequence step?

## Step 6: Rule in / rule out

Use clean statements like:
- Door sensor continuity tested good
- Door signal did not appear to reach the safety input
- Relay coil energized but contact output did not transfer
- PLC reset bit changed state but sequence did not progress

## Step 7: Finish with next action

End every investigation with one of these:
- repair wiring
- replace relay
- inspect controller fuse
- inspect PLC sequence/reset logic
- escalate for controller-specific service

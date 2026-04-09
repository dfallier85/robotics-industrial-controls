# Relay Testing Notes

## Main point

Do not assume a relay is good just because the coil has voltage.

A relay has two different sides:
- coil side
- contact side

Both matter.

## What to test

### 1. Coil voltage
Measure across the coil terminals, for example A1 to A2.

If the relay is supposed to energize, you should see rated voltage there.

### 2. Contact behavior
Measure across the contacts, for example:
- 11 to 14 on a normally open contact
- or continuity with power removed when appropriate

If coil voltage is present but contacts do not change as expected, the relay may be bad.

## Common mistake

People measure the coil, see 24 VDC, and stop there.

That only proves the relay is being told to energize.
It does not prove the switched path is actually changing.

## Practical advice

- Know whether the contact is NO or NC before testing
- Check the wiring diagram if available
- Trace from relay output all the way to controller input
- Do not confuse a terminal block with an internally linked relay contact

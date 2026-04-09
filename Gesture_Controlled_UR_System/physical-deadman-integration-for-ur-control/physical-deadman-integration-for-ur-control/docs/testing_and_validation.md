# Testing and Validation

## Goal

Verify that motion permission really depends on the physical deadman input.

## Good checks

- deadman active allows motion when other conditions are valid
- deadman false blocks motion
- releasing deadman during motion causes stop
- wrong input state is detected clearly
- suppression reason references deadman state
- reactivation requires deadman to be held again

## What to document

Write down:
- signal source used
- input mapping used
- active / inactive state meaning
- expected result
- actual observed result

## Good habit

Test both:
- success cases
- drop / release cases

The release case is where the deadman proves its value.

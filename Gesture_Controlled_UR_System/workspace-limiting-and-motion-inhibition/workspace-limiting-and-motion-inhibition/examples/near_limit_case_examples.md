# Near-Limit Case Examples

## Case 1: Near upper X limit

- Pose: `x = 0.58`
- Limit: `x_max = 0.60`
- Margin: `0.05`
- Requested: `+X`

Result:
- block `+X`

---

## Case 2: Near upper X limit, moving away

- Pose: `x = 0.58`
- Requested: `-X`

Result:
- allow `-X`

---

## Case 3: Near upper Z limit

- Pose: `z = 0.34`
- Limit: `z_max = 0.35`
- Margin: `0.05`
- Requested: `+Z`

Result:
- block `+Z`

---

## Case 4: Near upper X limit with mixed motion

- Pose: near `x_max`
- Requested: `+X +Y`

Result:
- block `+X`
- allow `+Y`

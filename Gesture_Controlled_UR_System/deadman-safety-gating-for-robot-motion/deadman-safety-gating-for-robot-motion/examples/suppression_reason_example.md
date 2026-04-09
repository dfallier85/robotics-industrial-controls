# Suppression Reason Example

## Scenario

User requests +Z motion near upper workspace limit.

## Example result

```text
requested: +Z
allowed: false
reason: +Z blocked by workspace limit
```

## Another example

```text
requested: +X
allowed: false
reason: deadman false
```

## Why this matters

The system becomes much easier to debug when blocked motion has a named reason.

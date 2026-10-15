# intent: Safe units-per-hour when hours is zero

- **Status:** accepted
- **Ticket:** TOY-1
- **Originator:** Data scientist (toy example)
- **Accepted by:** Repo owner — first walkthrough item

## What we want
`units_per_hour(units, 0)` currently crashes with ZeroDivisionError. It should handle zero
hours safely, and we want a ratio-of-sums aggregate across multiple shifts.

## Why now
It is the first item used to rehearse the full intent -> spec -> plan -> PR cycle.

## Constraints
- Keep the existing function signature.
- Behaviour for zero hours must be documented and tested.

## Out of scope
- Any other metrics. Any data loading.

## How we'll know it worked
- New tests for zero hours and the aggregate pass; existing tests still pass.
- The verifier subagent returns PASS.

## Open questions
- Should zero hours return `None` or `0.0`? (decide during spec)

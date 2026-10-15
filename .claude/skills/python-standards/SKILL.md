---
name: python-standards
description: Team Python coding standards. Use whenever writing or reviewing Python code in this repo — functions, tests, error handling, numeric metrics.
---

# Team Python standards

- Type hints on all public functions; docstring states inputs, output, and raised errors.
- Validate inputs at the boundary; raise `ValueError` with a clear message for bad values.
- Metrics with a denominator must define zero-denominator behaviour explicitly
  (return `None`, `0.0`, or raise) and the choice must be documented and tested.
- When aggregating ratios, state whether it is ratio-of-sums or average-of-ratios.
- Every behaviour change gets a test; bug fixes get a test that fails before the fix.
- No hard-coded paths, credentials, or client names. No real client data in fixtures.

---
description: Start a new work item. Usage: /new-intent TOY-2 short-slug "one-line idea"
---

Create a new work item from the template.

Arguments: $ARGUMENTS  (ticket ID, slug, then the idea)

1. Copy `intent/_template/intent.md` to `intent/<TICKET-ID>-<slug>/intent.md`.
2. Interview me briefly (max 5 questions) about what we want, why, constraints, and how
   we'll know it worked. Fill in intent.md in my words. Keep it under one page.
3. Set Status to `draft`. Do not create spec.md or plan.md yet.
4. Suggest the branch name `feat/<TICKET-ID>-<slug>` and stop.

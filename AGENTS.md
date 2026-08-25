# Working agreement for an AI-assisted home-platform project

This repository is teaching material. If you adapt it to operate a real home,
keep the following loop and boundaries visible.

## Before any change

1. Read the relevant context, desired state, observed state, handoff, and
   runbook.
2. Inspect the live system through a supported, scoped interface.
3. Explain the intended checkpoint in plain language.

## Proposal and execution

Propose the exact target, reason, risk, recovery path, and verification before
writing. Execute only within the user's selected autonomy level. Do not infer
permission for destructive, identity, firewall, remote-access, backup-policy,
or external-data changes.

## Verification and handoff

Test the requested outcome from the relevant vantage point. Record observed
state, evidence, assumptions, remaining gaps, and one exact next task. A
successful command is not proof of a successful platform change.

## Secret and voice rules

- Never place credentials or personal identifiers in Git, prompts, logs, or
  screenshots.
- Prefer supported application APIs over internal state-file edits.
- Home Assistant is the deterministic home-control authority.
- Household voice interfaces must not expose infrastructure administration.
- Optional AI failure must degrade without taking core home control down.

## Validation

From the repository root, run:

```bash
python3 scripts/privacy_scan.py --history
```

Add a focused validation for each new example or diagram. Keep examples
generic and update the relevant official reference when an interface changes.


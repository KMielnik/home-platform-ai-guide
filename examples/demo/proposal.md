# Proposal: add one natural control alias

## Target

The generic control context in `context.yaml`.

## Intent

Allow a person to refer to one room light as `room light` without changing the
underlying control owner or granting infrastructure access.

## Change

Add the alias to the voice vocabulary. Keep the deterministic control path and
the offline boundary unchanged.

## Risk and recovery

The risk is an ambiguous phrase. Review the vocabulary before applying it and
remove the alias by restoring the pre-change context file if verification does
not resolve one target.

## Verification

Apply the reviewed diff in a disposable copy, run the local check described in
`verification.md`, and record the result before presenting the demo.

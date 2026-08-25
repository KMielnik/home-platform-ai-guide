# Proposal: add a useful Assist alias

## Target

One existing light entity in the `Kitchen` area, exposed through Home
Assistant Assist.

## Intent

Let a household member say “turn on the kitchen light” without memorizing the
integration's canonical entity name.

## Change

Add the alias `kitchen light`, preserve the canonical name, and expose only the
light's normal on/off, brightness, and color controls.

## Risk

Low, but an ambiguous alias could target the wrong device if a second kitchen
light exists. Inspect the area and existing aliases first.

## Recovery

Restore the previous Assist exposure/alias configuration from the supported
Home Assistant backup or revert the reviewed configuration change.

## Verification

Test the phrase in the supported language, confirm the resolved entity, and
run a negative test for an internal diagnostic entity. Record the result and
timestamp in the observed-state report.


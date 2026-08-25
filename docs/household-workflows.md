# Household workflows and visual automation

Home control and household coordination overlap, but they are not identical.
Keep fast device actions in Home Assistant. A task or workflow service can
coordinate reminders, approvals, notifications, or external systems when that
is a real need.

## Decide where a workflow belongs

| Workflow | Natural owner |
| --- | --- |
| Turn lights on, set temperature, detect a door | Home Assistant |
| Notify a person after a condition | Home Assistant or a notification service |
| Assign a recurring household task | Task system |
| Join several external APIs with retries and approval | Visual workflow tool |
| Change infrastructure, firewall, backup, or identity | Operations runbook with human approval |

Avoid putting a safety-critical or latency-sensitive action behind a chain of
external workflows. The home should continue to function if the workflow
engine or an API provider is unavailable.

## Where a visual workflow tool fits

A tool such as n8n can be useful for visible, event-driven coordination and
API glue. Keep it downstream of the authoritative state, pin versions, store
credentials in its supported secret mechanism, and define retries and failure
notifications. Do not let a visual workflow become the only place where an
important household rule can be understood or recovered.

## A workflow contract

For every workflow record:

- trigger and expected input;
- idempotency rule;
- data and credential boundary;
- retry/backoff and dead-letter behavior;
- human approval points;
- output and notification;
- disable/restore procedure;
- owner and review date.


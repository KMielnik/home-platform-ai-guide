# Backups and restore proof

A snapshot is a useful point-in-time aid. It is not automatically an
independent backup, and a successful backup job is not proof that recovery
works. Design recovery around what must be rebuilt first.

## Classify data

| Class | Examples | Backup treatment |
| --- | --- | --- |
| Durable state | Home Assistant configuration, automations, device registry, secrets metadata, service databases | frequent, encrypted where appropriate, off-host |
| Rebuildable configuration | Compose/Ansible files, dashboards, documentation, scripts | version control plus an independent copy |
| Replaceable data | caches, generated thumbnails, temporary downloads | document the rebuild path; do not let it crowd out state |
| Bulk personal data | photos, documents, recordings | separate retention and privacy policy; test representative restores |

Never print secrets in a backup report. Store encryption keys so they can be
recovered without placing the only copy on the machine that may fail.

## Recovery order

```text
1. People, power, network, and a trusted recovery console
2. Host/storage and time
3. Operations control plane and secrets access
4. Home Assistant durable state
5. Protocol connectivity and critical automations
6. Monitoring and backup jobs
7. Optional services and replaceable data
```

The order is more useful than a list of tools. Write a one-page runbook that a
future operator can follow when tired.

## Proof loop

1. Record backup timestamp, scope, retention, and destination.
2. Inspect the archive metadata without exposing its contents unnecessarily.
3. Restore a representative database or configuration into a temporary,
   isolated directory.
4. Run integrity checks and compare expected files or records.
5. Exercise one documented application restore when safe.
6. Remove temporary material and record duration, gaps, and next action.

Test restoration from a different machine or account when that is part of the
real failure model. A backup that only works from the source host is a hidden
dependency.

## Alert on meaning

Useful alerts include backup older than policy, failed integrity check, low
recovery storage, and an encryption key that has no recovery copy. Avoid
alerting on every transient retry; escalation should correspond to an action.


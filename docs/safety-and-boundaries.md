# Safe AI operations

An agent can be excellent at inventory, explanation, test design, and
documentation while still being the wrong component to hold unrestricted
administrative power. Safety comes from architecture and process, not from a
promise that a model will always infer intent correctly.

## Narrow interfaces

Give the agent the smallest interface that can complete a checkpoint:

| Need | Prefer | Avoid |
| --- | --- | --- |
| Read health | read-only API or curated command | unrestricted shell as the default |
| Home control | Home Assistant Assist or a scoped service call | direct database edits |
| Configuration | version-controlled files and review | editing runtime state stores |
| Guest operations | scoped hypervisor API | generic root shell with delete/network powers |
| Backup | one documented job and a restore test | assuming a snapshot is a backup |
| Voice | household control intents | exposing maintenance and infrastructure tools |

Use separate credentials for inspection, routine operations, and recovery.
Keep recovery credentials offline or outside the system they recover. Never
put secrets in prompts, logs intended for sharing, screenshots, or Git.

## Autonomy levels

```text
Level 0  observe only
Level 1  propose a diff and wait
Level 2  execute reversible, low-risk maintenance
Level 3  execute approved runbook classes with automatic verification
Level 4  emergency recovery with a human-visible audit trail
```

Most new environments should start at Level 0 or 1. An unattended task should
still have a pre-declared change boundary, timeout, rollback, and evidence
requirement. “The command returned zero” is not enough verification.

## A proposal should be concrete

Before any write, state:

1. **Target** — exact host, service, file, or entity set.
2. **Intent** — the user-facing outcome.
3. **Change** — what will be modified.
4. **Risk** — likely impact and blast radius.
5. **Recovery** — backup, rollback, or console path.
6. **Verification** — test the outcome from a separate vantage point.
7. **Documentation** — where desired and observed state will be recorded.

If one of these is unknown, record the gap and narrow the action.

## Home Assistant boundary

Home Assistant should remain the home-control authority. Use its supported
interfaces and service calls. Do not edit its internal storage database by
hand. Keep internal integration plumbing, firmware actions, diagnostic
controls, and infrastructure tools away from household voice exposure unless a
specific reviewed use case requires them.

Voice aliases should sound natural, be unambiguous in the target language, and
be tested against the actual Assist pipeline. A phrase that is technically
unique but unnatural will fail in a real room.

## Human approval remains valuable

Require attended approval for changes that can:

- remove data or guests;
- alter routing, firewall, identity, or remote access;
- change backup policy or encryption;
- reboot the only management path;
- expose a new device or service to voice;
- spend money or send data to a new external provider.

An agent can prepare the commands and a rollback checklist. A person confirms
that the blast radius is acceptable.

## Safe failure

Every automation should fail closed where possible:

- an unavailable LLM must not prevent deterministic lights or climate control;
- an unavailable network must not erase local state;
- an ambiguous voice request should ask for clarification or do nothing;
- an incomplete backup should be clearly marked incomplete;
- a failed health check should stop the next dependent change.


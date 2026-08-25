# Build Your Own AI-First Home Platform

An intentionally generic, privacy-conscious teaching repository for people who
want to grow a Home Assistant installation into a maintainable home platform.
It explains the design habits that make an AI-assisted build useful without
turning an AI into an unbounded administrator:

> **source of truth + narrow interfaces + evidence + staged changes + AI
> assistance**

This is a talk and a set of practical notes, not a product catalogue or a
copy-and-paste homelab. It uses role-oriented examples so the design can fit an
old laptop, a mini PC, a workstation, a dedicated appliance, or no server at
all.

## What is here

- [The architecture guide](docs/architecture.md) — separate responsibilities
  without assuming a fixed number of machines.
- [Source of truth](docs/source-of-truth.md) — how intended, observed, and
  historical state work together.
- [Safe AI operations](docs/safety-and-boundaries.md) — narrow tools,
  approvals, recovery, and verification.
- [The build journey](docs/build-journey.md) — a staged path from discovery to
  optional voice and workflows.
- [Voice and Assist](docs/voice.md) — local speech, cloud reasoning, and safe
  household control.
- [Backups](docs/backups.md) and [monitoring](docs/monitoring.md) — evidence
  that the platform can be recovered and understood.
- [Lessons](docs/lessons.md) — the principles that generalize beyond one home.
- [`talk/slides.md`](talk/slides.md) — 35 editable slides with notes,
  section timings, and a complete 30–45 minute narrative.
- [`talk/demo-plan.md`](talk/demo-plan.md) — a live demo and a no-network
  fallback.
- [`scripts/privacy_scan.py`](scripts/privacy_scan.py) — a dependency-free
  privacy and secret scanner for the working tree and Git history.

## The smallest useful mental model

```text
                +------------------------------+
                | Source of truth              |
                | intent • vocabulary • policy |
                +---------------+--------------+
                                |
      +-------------------------+-------------------------+
      |                         |                         |
      v                         v                         v
+-------------+         +---------------+         +---------------+
| Home        |         | Operations    |         | Optional AI   |
| Assistant   |         | / control     |         | / voice       |
| deterministic|        | evidence, Git |         | local/cloud   |
| home control |        | backups, tests|         | speech/LLM    |
+-------------+         +---------------+         +---------------+
```

Home Assistant should stay the fast, deterministic home-control surface. An
operations agent can inspect and propose changes through explicitly scoped
interfaces. An AI or voice worker may add conversation and speech, but it does
not automatically receive infrastructure administration powers.

## Who this is for

Technical Home Assistant users, software developers, homelab builders, and
people who are comfortable following an AI-guided procedure while still
wishing to understand each checkpoint. The material also works as a talk for a
developer or internal engineering audience.

## How to use it

1. Read [source of truth](docs/source-of-truth.md) and [safety](docs/safety-and-boundaries.md).
2. Write down goals and constraints before choosing hardware or services.
3. Use the staged [build journey](docs/build-journey.md); stop at the smallest
   useful checkpoint.
4. Keep a human-readable record of desired state, observed state, evidence,
   and recovery.
5. Use the [talk](talk/README.md) as a guided tour, or adapt the slides for
   your own environment.

The repository deliberately avoids personal-home details, credentials,
network addresses, device identifiers, and private service names. Replace the
examples with your own values in a local, private project.

## Status and scope

This repository is educational material. It does not promise a universal
deployment recipe, and it does not itself install anything. Hardware,
operating systems, Home Assistant integrations, model availability, and
security guidance change over time; follow the official documentation linked
in [references](docs/references.md) before operating a live system.

## License

Documentation, diagrams, examples, and slides are licensed under
[CC BY 4.0](LICENSE). You may adapt them with attribution. Code in
`scripts/` is also covered by the repository license unless a file says
otherwise.


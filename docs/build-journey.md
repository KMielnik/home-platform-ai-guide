# A staged build journey

Build one layer manually, verify it, then automate the repeatable parts. The
phases below are checkpoints, not a demand to deploy every component.

## Phase 0 — Discovery and source of truth

Capture goals, constraints, vocabulary, hardware, power budget, network shape,
privacy preference, and recovery expectations. Create a Git repository with a
context file, an inventory, a handoff, and a short decision log.

**Exit evidence:** the user can explain what must be reliable, what may be
optional, and how to recover the first system.

## Phase 1 — Base host

Choose an appliance, a general-purpose operating system, or a hypervisor only
after comparing the operational cost. Record CPU, RAM, storage, network,
firmware, and power/thermal limits.

**Exit evidence:** management access, time synchronization, updates, and a
documented console/recovery path work.

## Phase 2 — Storage, network, and recovery

Classify durable configuration, replaceable application data, and disposable
cache. Define network ownership and remote access. Configure the first backup
destination before adding more services.

**Exit evidence:** a small restore into an isolated location succeeds.

## Phase 3 — Operations control plane

Add Git, a secrets workflow, a narrow management API, and a place for dated
observations. Ansible or another automation tool belongs here only after one
manual procedure is understood.

**Exit evidence:** the operator can inspect, propose, apply, and verify one
small change without guessing where the truth lives.

## Phase 4 — Home Assistant

Integrate devices by protocol and assign clear ownership. Keep entities
human-friendly and expose only useful controls/status to Assist. Preserve
backups before a broad refactor.

**Exit evidence:** core home-control flows work when optional AI services are
offline, and a recent backup is readable.

## Phase 5 — Optional household services

Add only services tied to a user goal: dashboards, calendars, task tracking,
energy, or an optional media role. Prefer pinned versions and documented
health checks. Keep replaceable data separate from home state.

**Exit evidence:** each service has an owner, a backup decision, a health check,
and a removal/rebuild path.

## Phase 6 — Repeatable configuration

Turn the stable manual procedure into declarative files or Ansible. Validate
configuration before applying it. Keep secrets external and use small
checkpoints so a diff has one reason.

**Exit evidence:** a second run is idempotent or its non-idempotence is
documented.

## Phase 7 — Backups and restore proof

Back up durable state, metadata, and configuration to an independent
destination. Set retention and alert on freshness. Restore representative
databases/files into a temporary location and clean up afterward.

**Exit evidence:** a timed restore exercise produces a usable result and a
human knows the recovery order.

## Phase 8 — Monitoring

Monitor reachability, service health, storage space, backup freshness,
hardware temperatures, and the signals that matter to the user. Keep alerts
actionable; a dashboard full of trivia is not reliability.

**Exit evidence:** a deliberately stopped test service produces the expected
signal and recovery is observed.

## Phase 9 — Voice and AI worker

Add local speech or a cloud model only after deterministic Home Control is
stable. Benchmark on actual language, rooms, latency, and privacy needs.
Separate conversational access from infrastructure administration.

**Exit evidence:** voice still controls the important home functions when the
optional LLM is unavailable, and the fallback is understood.

## Phase 10 — Optional workflows

Introduce visual workflow tools, task systems, and external integrations only
when a repeated human workflow justifies them. Keep them downstream of the
source of truth and avoid making them the sole owner of durable state.

**Exit evidence:** a workflow has a retry/error path, a human-readable audit,
and no hidden credential sprawl.

## Phase 11 — Future extensions

Consider energy optimization, extra sensors, model serving, on-demand compute,
or hardware migration. Write a proposal and an experiment plan before making
the production change.

## When to stop

Stop at the smallest checkpoint that solves the current problem. A simple,
well-backed-up appliance is a better platform than a sophisticated stack that
no one can restore.


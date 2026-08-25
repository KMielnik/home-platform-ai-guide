# Lessons that generalize

## Complexity is a design signal

The fun of integrating one device can turn into work when devices, rooms,
protocols, dashboards, servers, backups, monitoring, voice, and AI all interact.
When that happens, name the roles and ownership boundaries before adding the
next tool.

## Source of truth reduces AI rediscovery

Every future session otherwise pays for the same archaeology: what is the
hardware, which service owns a setting, what is safe to restart, when was the
last backup, and what is intentionally deferred? A concise, current repository
turns that repeated discovery into a quick verification pass.

## Build one layer manually

Automation written before the operator understands the manual behavior hides
assumptions. Do one checkpoint by hand, capture evidence, then automate the
repeatable part and test idempotence.

## Hardware migrations reveal boundaries

When a workload moves between an appliance, VM, container, or GPU worker, clear
ownership and recovery paths matter more than the original topology. Role-based
design makes a migration a placement change instead of a total rebuild.

## Bigger is not automatically better

Language model quality, speech accuracy, and perceived responsiveness depend on
the actual language, room, hardware, and intent. Benchmark representative
interactions; route deterministic control around the model when possible.

## Voice should not become an admin console

Natural language is an excellent household interface and a poor authorization
boundary for destructive infrastructure operations. Keep the two planes
separate.

## Recovery is a feature

Backups, restore exercises, monitoring, and an emergency console are not
polish. They determine whether a failed experiment is a short interruption or
an unexplained weekend.

## Local and cloud can coexist

Privacy, cost, latency, quality, and maintenance are different axes. A hybrid
route can keep home control local while using external reasoning only for the
requests that benefit from it.

## Evidence beats confidence

An agent can explain a plausible plan while being wrong about a live system.
Inspect the real state, test the requested outcome from the right vantage point,
and record what was actually verified.


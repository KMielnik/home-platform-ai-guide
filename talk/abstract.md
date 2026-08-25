# Abstract and meetup description

## Short abstract

Home Assistant is easy to love and surprisingly hard to maintain once devices,
automations, servers, backups, voice, and AI enter the picture. This talk
shows how to turn that growth into a role-oriented platform that remains
understandable: Home Assistant handles fast deterministic control; a small
operations control plane keeps source of truth, evidence, recovery, and narrow
agent interfaces; optional local or cloud AI adds speech and conversation
without becoming an infrastructure admin console.

The central lesson is simple: **source of truth + narrow interfaces + evidence
+ staged changes + AI assistance**. We will follow a build journey from an
empty home-server machine through recovery, monitoring, voice, benchmarking,
on-demand compute, and household workflows. The examples are intentionally
generic so the approach can adapt to a mini PC, an old laptop, an appliance, or
a larger homelab.

## Meetup description

Home Assistant starts as a delightful weekend project. Then the device count
grows, integrations multiply, and the system begins to need the same things as
any small platform: ownership, backups, monitoring, documentation, and a safe
way to change it.

In this practical, architecture-focused talk, we will explore how an AI agent
can help inventory hardware, explain trade-offs, propose changes, run bounded
checks, and keep a source-of-truth repository current. We will also cover voice
architecture, local versus cloud speech and language models, hybrid routing,
and why a household assistant must not inherit hypervisor or container
administration powers.

Attendees leave with a staged build model and a set of questions to adapt it to
their own hardware, network, privacy preferences, and budget.

## Audience and prerequisites

Technical Home Assistant users, developers, and homelab builders. No specific
hardware or model is required. Familiarity with Git and basic Linux concepts is
helpful but not essential.


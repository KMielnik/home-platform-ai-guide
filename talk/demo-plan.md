# Demo plan and fallback

The demo is designed to prove the method, not to show a particular private
installation. Use a disposable or simulated Home Assistant workspace and
generic names such as `Kitchen light` and `Hall temperature`.

## Live path (about five minutes)

### 1. Read the source of truth (45 seconds)

Show the context, desired-state, and observed-state files. Point out that the
agent can answer “what is this system?” without rediscovering it from chat.

### 2. Inspect before changing (60 seconds)

Run a read-only health check or show a captured observation. Ask the audience
what evidence would be missing if the command merely returned success.

### 3. Propose a narrow change (60 seconds)

Use a generic request: expose a useful room light to Assist and add a natural
alias. Show target, reason, risk, backup, and verification before execution.

### 4. Verify the outcome (60 seconds)

Run a deterministic Assist query or a simulated test, then show the changed
observed-state report. Demonstrate that an internal diagnostic entity was not
made voice-visible just because it existed.

### 5. Show recovery evidence (45 seconds)

Display backup freshness and a sample isolated restore result. Explain that
the restore proof is more persuasive than a green scheduler badge.

## Preparation checklist

- Use a disposable tenant or pre-recorded sanitized output.
- Disable outbound calls if the venue network is untrusted.
- Remove all personal names, addresses, device identifiers, and account data.
- Keep the presentation and a terminal recording available offline.
- Prepare a known-good branch or copy of the demo files.
- Never type a real credential during the talk.

## Offline fallback (three-minute core; five-minute slot variant)

Open [`examples/demo/`](../examples/demo/) and walk through its six artifacts
in order: [`context.yaml`](../examples/demo/context.yaml),
[`inventory.yaml`](../examples/demo/inventory.yaml),
[`proposal.md`](../examples/demo/proposal.md),
[`change.diff`](../examples/demo/change.diff),
[`verification.md`](../examples/demo/verification.md), and
[`restore-evidence.md`](../examples/demo/restore-evidence.md). From that
directory, run the read-only Python check in its README to prove the package is
complete without network access. Then show the Mermaid voice and role
diagrams. The audience still sees the core loop even if the network, model,
microphone, or projector fails.

The core walkthrough fits three minutes. In the live-demo timing variant, use
the remaining two minutes to pause on the proposal and restore evidence.

## Failure narration

If a demo step fails, say what the evidence means: “The optional model is
unavailable; deterministic control should still work.” Do not improvise a
production fix in front of an audience. Switch to the fallback and record the
failure for later analysis.

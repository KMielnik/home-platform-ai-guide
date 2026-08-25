# Contributing

Contributions should make the core lesson clearer:

> source of truth + narrow interfaces + evidence + staged changes + AI
> assistance.

## Before opening a change

- Read the relevant document and its links to official primary sources.
- Prefer a small, teachable change over a large framework.
- Use generic role-oriented examples; do not copy a real home's topology.
- Do not add secrets, addresses, usernames, account identifiers, serials,
  screenshots with private data, or private service names.
- Run `python3 scripts/privacy_scan.py` from the repository root.

## Documentation style

Use plain language, state assumptions, and separate facts from examples.
Explain why a boundary exists before showing a command. Commands should be
safe to review and should not depend on a particular person's paths or
credentials. Link to the vendor's official documentation for changing
interfaces instead of reproducing large excerpts.

## Pull requests

Describe the problem, the teaching outcome, privacy impact, and validation
performed. If a diagram or slide changes, mention the audience takeaway and
the approximate timing impact. A reviewer should be able to reproduce the
validation without access to a private home.


# Security and privacy

This repository is public teaching material, not an operations endpoint. It
contains no credentials and intentionally avoids real home identifiers.

## Reporting an issue

If you find a secret, personal data, a private address, or a detail that could
make a real home easier to identify, do not open a public issue containing the
value. Remove it from any local copy, then contact the repository maintainer
through the platform's private security channel. If no private channel exists,
open an issue that describes the file and category without reproducing the
value.

## Safe use

- Treat every command as an example; review it for your operating system.
- Keep management interfaces on a trusted administrative path.
- Use least privilege and explicit approvals for changes.
- Keep recovery credentials outside the machine they recover.
- Do not give a household voice agent direct access to hypervisor, container,
  Docker, SSH, or backup administration.
- Test backups by restoring into an isolated location before trusting them.

Run the local privacy gate before sharing a fork:

```bash
python3 scripts/privacy_scan.py
```


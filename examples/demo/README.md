# Offline fallback package

This directory is a complete, generic six-artifact fallback for the live demo.
It needs only a checkout and a local Python 3 interpreter; it makes no network
requests and does not represent a real household.

The artifacts are deliberately one role each:

1. [`context.yaml`](context.yaml) — context and boundaries.
2. [`inventory.yaml`](inventory.yaml) — available roles and capabilities.
3. [`proposal.md`](proposal.md) — the reviewed target and recovery path.
4. [`change.diff`](change.diff) — the proposed diff/change.
5. [`verification.md`](verification.md) — outcome evidence.
6. [`restore-evidence.md`](restore-evidence.md) — isolated restore evidence.

## Run it offline

From this directory, run the following read-only check:

```bash
git apply --check change.diff
python3 - <<'PY'
from pathlib import Path

expected = (
    "context.yaml",
    "inventory.yaml",
    "proposal.md",
    "change.diff",
    "verification.md",
    "restore-evidence.md",
)
root = Path.cwd()
missing = [name for name in expected if not (root / name).is_file()]
if missing:
    raise SystemExit(f"missing artifact(s): {', '.join(missing)}")
print(f"{len(expected)} artifacts present")
print("offline fallback package: PASS")
PY
```

For the talk, open the files in order, explain the proposal before showing the
diff, then use the verification and restore evidence to close the loop.

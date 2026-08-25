#!/usr/bin/env python3
"""Small dependency-free privacy gate for this public teaching repository.

The restricted-vocabulary table contains only one-way fingerprints.  The
scanner normalizes candidate text, fingerprints each possible substring, and
checks the working tree plus (on request) reachable Git blobs and commit
metadata.  It therefore enforces the gate without publishing the restricted
vocabulary in the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]


# Store only SHA-256 fingerprints of normalized terms.  The first value is the
# normalized length; it lets the scanner test candidate windows without
# retaining a reversible representation of the term.
DENYLIST_FINGERPRINTS: tuple[tuple[int, str], ...] = (
    (8, "60526b742a568968d26c653242180d8d86e4dc2838b752374faaa6448539f7bb"),
    (6, "7da0324ce46c55f7dcfee581bb13cd5bc66cc4d514dcd1cd03bb9008b8b2f517"),
    (6, "f3bbc5fe1699edd8989888b985f5036dd2fddcc9c96114d11678bf87b24bf113"),
    (6, "d377d500e1e178f39b6ca8c57b3e702bef1c167d98f86ecddb0d418e78b0efb4"),
    (8, "39a0be6d6589d78d28dde15fe6d6de95fa18a1d7cd323cfe6a72e700333c35c5"),
    (5, "174f438bb5d1528c9f03782f448b60db4d01142fc5f80dfb88c3ee48c866db3d"),
    (5, "6ad309b484c58917daa8153945db5411cb31adfec6e19fe7e6e49079cb4f2951"),
    (11, "e851219b75c97d1a161ad6b20c05b82cabb6c3b1b5ab542d9538d0fb1f31ba88"),
    (7, "575e2265619125a7586b8cbbad1f83026c224af5276a84e76533b29a3a743d33"),
    (6, "194448e2770cf0f7ce48930cf13794a7c6ac14d36ec0adfbfb8ee8397187a87f"),
    (9, "d2132690e5fda8b57522797c120c6cb11613f58a5d9f6330a828e9fa0b10a397"),
)

# A seed repository may have been created with this conventional placeholder
# identity.  It is not a personal address; real addresses still fail below.
GENERIC_METADATA_EMAILS = {"noreply" + "@" + "example.invalid"}


PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "private IPv4 address",
        re.compile(
            r"(?<![\d.])(?:10(?:\.\d{1,3}){3}|127(?:\.\d{1,3}){3}|"
            r"169\.254(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])"
            r"(?:\.\d{1,3}){2}|192\.168(?:\.\d{1,3}){2})(?![\d.])"
        ),
    ),
    ("MAC address", re.compile(r"(?i)\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b")),
    (
        "email address",
        re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    ),
    ("Tailscale domain", re.compile(r"(?i)\b[a-z0-9.-]+\.ts\.net\b")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("common access token", re.compile(r"(?i)\b(?:sk|gh[pousr]|xox[baprs])-[A-Za-z0-9_-]{16,}\b")),
    ("cloud access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
)


@dataclass(frozen=True)
class Finding:
    source: str
    line: int
    category: str
    excerpt: str


def is_binary(data: bytes) -> bool:
    return b"\0" in data


def normalize(value: str) -> str:
    """Return a case- and separator-insensitive comparison form."""

    folded = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in folded if character.isalnum())


def restricted_term_present(value: str) -> bool:
    """Check normalized substring windows against the one-way fingerprints."""

    candidate = normalize(value)
    for length, expected in DENYLIST_FINGERPRINTS:
        if length > len(candidate):
            continue
        for start in range(len(candidate) - length + 1):
            window = candidate[start : start + length].encode("utf-8")
            if hashlib.sha256(window).hexdigest() == expected:
                return True
    return False


def scan_text(source: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()
    for number, line in enumerate(lines, start=1):
        if restricted_term_present(line):
            findings.append(Finding(source, number, "restricted term", line.strip()[:160]))
        for category, pattern in PATTERNS:
            if pattern.search(line):
                findings.append(Finding(source, number, category, line.strip()[:160]))
    return findings


def working_tree_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if not is_binary(data):
            files.append(path)
    return files


def scan_working_tree() -> list[Finding]:
    findings: list[Finding] = []
    for path in working_tree_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        findings.extend(scan_text(str(path.relative_to(ROOT)), text))
    return findings


def scan_git_history() -> list[Finding]:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "rev-list", "--objects", "--all"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return []
    if result.returncode != 0:
        return []

    findings: list[Finding] = []
    seen: set[str] = set()
    for item in result.stdout.splitlines():
        pieces = item.split(" ", 1)
        if len(pieces) != 2 or pieces[0] in seen:
            continue
        object_id, path = pieces
        seen.add(object_id)
        blob = subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "blob", object_id],
            check=False,
            capture_output=True,
        )
        if blob.returncode != 0 or is_binary(blob.stdout):
            continue
        try:
            text = blob.stdout.decode("utf-8")
        except UnicodeDecodeError:
            continue
        findings.extend(scan_text(f"git:{path}", text))
    return findings


def scan_git_metadata() -> list[Finding]:
    """Scan reachable commit subjects/bodies and identity fields.

    Commit metadata is separate from blob content, so it needs its own pass.
    A repository seed may use the documented generic placeholder address; any
    other address is treated as a possible identity leak.
    """

    format_string = "%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%B%x1e"
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--all", f"--format={format_string}"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return []
    if result.returncode != 0:
        return []

    findings: list[Finding] = []
    for record in result.stdout.split("\x1e"):
        fields = record.split("\x1f", 5)
        if len(fields) != 6:
            continue
        object_id, author_name, author_email, committer_name, committer_email, body = fields
        for label, value in (
            ("author", author_name),
            ("committer", committer_name),
            ("message", body),
        ):
            findings.extend(scan_text(f"git-meta:{object_id}:{label}", value))
        for label, value in (
            ("author-email", author_email),
            ("committer-email", committer_email),
        ):
            if value.casefold() in GENERIC_METADATA_EMAILS:
                continue
            findings.extend(scan_text(f"git-meta:{object_id}:{label}", value))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan this repository for public-data hazards")
    parser.add_argument("--history", action="store_true", help="also scan reachable Git blobs")
    args = parser.parse_args()

    findings = scan_working_tree()
    if args.history:
        findings.extend(scan_git_history())
        findings.extend(scan_git_metadata())

    if findings:
        print(f"privacy scan: FAIL ({len(findings)} finding(s))")
        for finding in findings:
            print(f"{finding.source}:{finding.line}: {finding.category}: {finding.excerpt}")
        return 1

    files = len(working_tree_files())
    history_note = " and Git history" if args.history else ""
    print(f"privacy scan: PASS ({files} text files scanned{history_note})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

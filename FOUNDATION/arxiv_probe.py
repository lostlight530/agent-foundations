#!/usr/bin/env python3
"""Fetch arXiv identity/version provenance with only the Python standard library.

The helper is intentionally explicit and manually invoked. It exists so Jules can
verify an arXiv identifier, title, authors, and version-specific date without creating
one-off downloader scripts or relying on truncated search snippets.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

USER_AGENT = "Mozilla/5.0 AgentFoundationsProvenanceProbe/1.0"
ARXIV_ID_RE = re.compile(r"^(?P<base>\d{4}\.\d{4,5})(?:v(?P<version>\d+))?$")
VERSION_RE = re.compile(r"\[v(?P<version>\d+)\]\s*(?P<stamp>[^\[]+?UTC)")
ATOM = {"atom": "http://www.w3.org/2005/Atom"}


def normalize_arxiv_id(value: str) -> tuple[str, int | None]:
    value = value.strip()
    for prefix in ("arXiv:", "https://arxiv.org/abs/", "http://arxiv.org/abs/"):
        if value.startswith(prefix):
            value = value[len(prefix):]
    value = value.rstrip("/")
    match = ARXIV_ID_RE.fullmatch(value)
    if not match:
        raise ValueError(f"unsupported arXiv identifier: {value!r}")
    version = int(match.group("version")) if match.group("version") else None
    return match.group("base"), version


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/atom+xml,text/html;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def api_metadata(base_id: str) -> dict[str, object]:
    query = urllib.parse.urlencode({"id_list": base_id})
    payload = fetch_text(f"https://export.arxiv.org/api/query?{query}")
    root = ET.fromstring(payload)
    entry = root.find("atom:entry", ATOM)
    if entry is None:
        raise RuntimeError(f"arXiv API returned no entry for {base_id}")

    def atom_text(name: str) -> str:
        node = entry.find(f"atom:{name}", ATOM)
        return " ".join((node.text or "").split()) if node is not None else ""

    authors = [
        " ".join((node.text or "").split())
        for node in entry.findall("atom:author/atom:name", ATOM)
        if (node.text or "").strip()
    ]
    return {
        "api_id": atom_text("id"),
        "title": atom_text("title"),
        "authors": authors,
        "published": atom_text("published"),
        "updated": atom_text("updated"),
    }


def version_history(base_id: str) -> list[dict[str, object]]:
    page = fetch_text(f"https://arxiv.org/abs/{base_id}")
    visible = html.unescape(re.sub(r"<[^>]+>", " ", page))
    visible = " ".join(visible.split())

    versions: list[dict[str, object]] = []
    seen: set[int] = set()
    for match in VERSION_RE.finditer(visible):
        version = int(match.group("version"))
        if version in seen:
            continue
        seen.add(version)
        stamp = " ".join(match.group("stamp").split())
        try:
            parsed = parsedate_to_datetime(stamp.replace(" UTC", " +0000"))
            iso_date = parsed.date().isoformat()
        except (TypeError, ValueError, OverflowError):
            iso_date = None
        versions.append({"version": version, "timestamp": stamp, "date": iso_date})

    versions.sort(key=lambda item: int(item["version"]))
    return versions


def probe(value: str) -> dict[str, object]:
    base_id, requested_version = normalize_arxiv_id(value)
    result: dict[str, object] = {
        "requested": value,
        "base_id": base_id,
        "requested_version": requested_version,
        "user_agent": USER_AGENT,
    }
    result.update(api_metadata(base_id))
    result["versions"] = version_history(base_id)
    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_id", help="arXiv ID, optionally with vN")
    parser.add_argument("--expect-version", type=int, help="require a specific version to exist")
    parser.add_argument("--expect-date", help="require YYYY-MM-DD for the requested/expected version")
    args = parser.parse_args(argv[1:])

    try:
        result = probe(args.arxiv_id)
    except Exception as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 2

    requested_version = result["requested_version"]
    expected_version = args.expect_version if args.expect_version is not None else requested_version
    history = {int(item["version"]): item for item in result["versions"]}

    errors: list[str] = []
    if expected_version is not None and expected_version not in history:
        errors.append(f"version v{expected_version} not found in submission history")
    if args.expect_date:
        if expected_version is None:
            errors.append("--expect-date requires a version in the ID or --expect-version")
        elif expected_version in history and history[expected_version].get("date") != args.expect_date:
            errors.append(
                f"v{expected_version} date is {history[expected_version].get('date')!r}, expected {args.expect_date!r}"
            )

    result["status"] = "VERIFIED" if not errors else "MISMATCH"
    result["errors"] = errors
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

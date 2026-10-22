#!/usr/bin/env python3
"""Render a Markdown scorecard from an AI-visibility results.json file.

Usage:
    python3 scripts/scorecard.py results.json [previous_results.json] > scorecard.md

Standard library only. See examples/acme-widgets.results.json for the schema.
"""
from __future__ import annotations

import json
import sys
from collections import Counter

ENGINE_ORDER = ["chatgpt", "gemini", "google_ai_mode", "perplexity"]


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _engines(data: dict) -> list[str]:
    seen = {r["engine"] for r in data.get("results", [])}
    ordered = [e for e in ENGINE_ORDER if e in seen]
    return ordered + sorted(seen - set(ordered))


def _cell(r: dict | None) -> str:
    if r is None:
        return "–"
    if r.get("status") == "failed":
        return "FAILED"
    if r.get("mentioned"):
        return f"✅ #{r['rank']}" if r.get("rank") else "✅"
    return "❌"


def summarize(data: dict) -> dict:
    """Hit rates per engine, counting failed calls separately (never as misses)."""
    per_engine: dict[str, dict] = {}
    for e in _engines(data):
        rows = [r for r in data["results"] if r["engine"] == e]
        ok = [r for r in rows if r.get("status") != "failed"]
        hits = [r for r in ok if r.get("mentioned")]
        per_engine[e] = {
            "asked": len(rows),
            "failed": len(rows) - len(ok),
            "valid": len(ok),
            "mentioned": len(hits),
            "hit_rate": (len(hits) / len(ok)) if ok else None,
        }
    valid = sum(v["valid"] for v in per_engine.values())
    mentioned = sum(v["mentioned"] for v in per_engine.values())
    competitors = Counter(
        c for r in data["results"] if r.get("status") != "failed" for c in r.get("competitors", [])
    )
    sources = Counter(
        s for r in data["results"] if r.get("status") != "failed" for s in r.get("third_party_sources", [])
    )
    return {
        "per_engine": per_engine,
        "overall_hit_rate": (mentioned / valid) if valid else None,
        "competitors": competitors.most_common(),
        "third_party_sources": sources.most_common(),
    }


def _pct(x: float | None) -> str:
    return "n/a" if x is None else f"{x * 100:.0f}%"


def diff(curr: dict, prev: dict) -> list[str]:
    def key(r):
        return (r["engine"], r["question_id"])

    old = {key(r): r for r in prev.get("results", []) if r.get("status") != "failed"}
    lines = []
    for r in curr.get("results", []):
        if r.get("status") == "failed" or key(r) not in old:
            continue
        o = old[key(r)]
        if bool(o.get("mentioned")) != bool(r.get("mentioned")):
            state = "now mentioned" if r.get("mentioned") else "no longer mentioned"
            lines.append(f"- {r['engine']} / {r['question_id']}: {state}")
        elif r.get("mentioned") and o.get("rank") != r.get("rank"):
            lines.append(f"- {r['engine']} / {r['question_id']}: rank {o.get('rank')} → {r.get('rank')}")
    old_comp = {c for r in old.values() for c in r.get("competitors", [])}
    new_comp = sorted(
        {c for r in curr.get("results", []) if r.get("status") != "failed" for c in r.get("competitors", [])}
        - old_comp
    )
    if new_comp:
        lines.append("- New competitors: " + ", ".join(new_comp))
    return lines or ["- No changes."]


def render(data: dict, prev: dict | None = None) -> str:
    s = summarize(data)
    engines = _engines(data)
    idx = {(r["engine"], r["question_id"]): r for r in data.get("results", [])}
    out = [f"# AI Visibility Scorecard — {data.get('brand', 'Unknown brand')}", ""]
    if data.get("date"):
        out += [f"Audit date: {data['date']}", ""]
    out += [f"**Overall hit rate (valid answers only): {_pct(s['overall_hit_rate'])}**", ""]

    out += ["## Engine × question", "", "| Question | " + " | ".join(engines) + " |",
            "|---|" + "---|" * len(engines)]
    for q in data.get("questions", []):
        label = f"{q['id']} ({q.get('type', 'intent')}): {q['text']}"
        out.append(f"| {label} | " + " | ".join(_cell(idx.get((e, q["id"]))) for e in engines) + " |")
    out.append("")

    out += ["## Hit rate by engine", "", "| Engine | Asked | Failed | Mentioned | Hit rate |", "|---|---|---|---|---|"]
    for e, v in s["per_engine"].items():
        out.append(f"| {e} | {v['asked']} | {v['failed']} | {v['mentioned']}/{v['valid']} | {_pct(v['hit_rate'])} |")
    out.append("")

    out += ["## Competitors named by AI engines", ""]
    out += [f"- {c} ({n})" for c, n in s["competitors"]] or ["- None recorded."]
    out += ["", "## Third-party sources cited", ""]
    out += [f"- {c} ({n})" for c, n in s["third_party_sources"]] or ["- None recorded."]

    if prev is not None:
        out += ["", "## Compared with last audit", ""] + diff(data, prev)
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print(__doc__, file=sys.stderr)
        return 2
    prev = load(argv[2]) if len(argv) == 3 else None
    sys.stdout.write(render(load(argv[1]), prev))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

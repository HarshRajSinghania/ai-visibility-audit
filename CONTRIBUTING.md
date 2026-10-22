# Contributing

Thanks for helping! Useful contributions:

- **Provider adapters / notes**: how to get answer + citations or keyword data from
  another provider (API, MCP connector, or manual workflow), mapped to the
  `results.json` schema in `examples/`.
- **Better question sets** for specific industries (keep them brand-neutral).
- **Scorecard improvements** in `scripts/scorecard.py` (standard library only).
- Bug reports and doc fixes.

## Ground rules

- Never commit API keys, tokens, real customer data, or private audit results.
  Use fictional brands (e.g. "Acme Widgets") and `.example` domains in examples.
- Keep the skill analysis-only and budget-capped.
- Run `python3 -m unittest discover -s tests` before opening a PR.
- Add a line to `CHANGELOG.md` under "Unreleased".

## Process

1. Open an issue describing the change (optional for small fixes).
2. Fork, branch, commit, open a PR. Small, focused PRs are reviewed fastest.

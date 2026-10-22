# Example prompts

Basic:

```text
Run the ai-visibility-audit skill for "Acme Widgets" (domain acme-widgets.example).
Market: US. Product scope: industrial widgets, custom sizes. Budget: USD 1.
Write the report in English to ./audit-2026-01/.
```

Repeat audit with comparison:

```text
Re-run ai-visibility-audit for "Acme Widgets" with the same questions as
./audit-2026-01/results.json. Budget USD 0.50. Add a "Compared with last audit"
section and save to ./audit-2026-04/.
```

No paid provider (manual mode):

```text
Run ai-visibility-audit for "Acme Widgets" in manual mode: draft the questions,
then give me a checklist to paste each engine's answer back to you, and build the
report from what I paste.
```

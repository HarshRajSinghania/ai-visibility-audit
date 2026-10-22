# AI Visibility & SEO Audit — Acme Widgets (FAKE EXAMPLE)

> Acme Widgets is fictional. Every number below is invented to illustrate the format.

- Date: 2026-01-15 · Market: US · Domain: acme-widgets.example · Budget/spent: USD 1.00 / USD 0.21

## 3. AI answer visibility
See `acme-widgets.scorecard.md`. Overall hit rate 60% (3 of 5 valid answers); 1 call failed.

- [Measured] Acme is named for its own brand question on both engines, but on
  only 1 of 4 valid buying-intent answers (ChatGPT Q2, rank 3).
- [Measured] "Globex Widgets" is the most-named competitor (3 answers).
- [Inferred] Engines lean on `directory.example` and `forum.example` for generic
  questions; Acme has no presence there.

## 7. Improvement list
| # | Action | Where | Why (evidence) | Priority |
|---|---|---|---|---|
| 1 | Add Organization + Product JSON-LD | site templates | No structured data found [Measured] | High |
| 2 | Publish a "custom sizes & lead times" page with concrete specs | /custom | Only intent question where Acme appears [Measured] | High |
| 3 | Claim/complete listing on directory.example | external | Cited in 2 intent answers [Measured] | Medium |
| 4 | Add `llms.txt` summarizing products | site root | Missing [Measured]; impact uncertain [Inferred] | Low |

## 9. Cost ledger
| Endpoint | Unit price (USD) | Calls | Charged | Notes |
|---|---|---|---|---|
| ai-answer (example) | 0.01 | 6 | 0.05 | 1 failed, not charged |
| keywords (example) | 0.08 | 2 | 0.16 | |

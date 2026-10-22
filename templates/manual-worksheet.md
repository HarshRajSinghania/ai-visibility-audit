# Manual AI visibility worksheet

Use this worksheet with a text editor, a browser, and Python. No API key,
subscription, or paid data source is required. If an engine is unavailable for
free, record that limit; do not purchase access to complete the worksheet.
Acme Widgets and `acme-widgets.example` below are fictional placeholders, not an
observed business. This worksheet contains no measurement results.

## 1. Define the audit

- Brand and exact aliases to recognize: [fill in privately]
- Owned domains: [fill in privately]
- Product scope and buyer type: [fill in]
- Market, language, and location: [fill in]
- Audit date (YYYY-MM-DD), time, and timezone: [fill in]
- Engines planned: [fill in]
- Browser/session conditions, account state, model or mode if shown: [fill in]
- Paid calls: none in this workflow; do not enable a paid tool.

Keep real audit files outside the source repository. Do not publish private
answers, personal details, account identifiers, credentials, or customer data.

## 2. Choose questions before observing answers

Use five or more buying-intent questions and one brand question. Keep wording
and IDs fixed when repeating an audit. Record changes instead of silently
comparing different questions. The fictional example below is a prompt only.

| ID | Type | Exact question |
|---|---|---|
| Q1 | intent | Which industrial widget suppliers support small production runs? |
| Q2 | intent | [fill in] |
| Q3 | intent | [fill in] |
| Q4 | intent | [fill in] |
| Q5 | intent | [fill in] |
| Q6 | brand | What evidence is available about Acme Widgets? |

## 3. Collect evidence manually

1. Open a fresh conversation for each question. Record the visible engine/mode,
   date, locale, and login state. Do not imply a fresh session removes all bias.
2. Submit the exact question once and save the complete answer and citations in
   a private local evidence file. Note retries and retain the failed attempt log.
3. Mark a brand mention only when it matches the predefined brand or aliases.
   A citation to an owned domain alone is not a brand-name mention.
4. Record rank only for an explicit ordered recommendation list; otherwise use
   `null`. Copy citations as shown. Do not invent missing URLs or sources.
5. Record errors, access restrictions, or absent answers separately. A failed
   attempt is never a negative brand observation.

Copy this row for each question/engine pair:

| Question ID | Engine | Time/session | Attempt outcome | Evidence file | Mentioned? | Rank | Name used | Cited URLs | Competitors | Third-party sources | Error/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ID] | [engine] | [conditions] | [ok / failed / not attempted] | [private relative reference] | [true / false / unknown] | [number / null] | [exact name / null] | [copied list] | [exact names or domains] | [source domains] | [reason] |

## 4. Map observations to results.json

- Root fields: `brand`, `date`, `market`, `questions`, and `results` are required.
  `aliases` and `domains` are optional string lists.
- Each question needs `id`, `type` (`intent` or `brand`), and `text`.
- Engine IDs: `chatgpt`, `gemini`, `google_ai_mode`, `perplexity`, or another
  consistent string. Record the displayed model/mode in private provenance.
- An `ok` row needs `engine`, `question_id`, `status`, and boolean `mentioned`.
  Optional fields: `rank` (positive integer or null), `name_used` (string or
  null), and string lists `cited_urls`, `competitors`, `third_party_sources`.
  If not mentioned, rank must be null or absent.
- A `failed` row needs `engine`, `question_id`, `status`, and a nonempty `error`.
  Do not convert unknown observations to `mentioned: false`.
- For `not attempted`, omit the result row and explain the missing coverage in
  the worksheet. The report shows a dash for absent engine/question pairs when
  the engine has another recorded observation.
- Keep one final result per question/engine pair; retain retry history in the
  evidence log. Question IDs must be unique and references must exist.

Starter JSON (fictional identity and placeholder date; replace them privately):

```json
{
  "brand": "Acme Widgets",
  "aliases": ["Acme Widgets"],
  "domains": ["acme-widgets.example"],
  "date": "2026-01-15",
  "market": "US",
  "questions": [
    {"id": "Q1", "type": "intent", "text": "Which industrial widget suppliers support small production runs?"}
  ],
  "results": []
}
```

Add the remaining questions before collecting answers. Empty results mean no
observations and an `n/a` hit rate, not zero visibility.

From the project root, render a private audit folder adjacent to the checkout:

```bash
python3 scripts/scorecard.py ../private-audit/results.json > ../private-audit/scorecard.md
```

Create that folder and save results first. A validation error names the field
and exits with code 2. Keep `scripts/` and `schema/` together.

## 5. Optional search evidence

Manual search observations or an export from a search tool you already have
may supplement the audit. Record query, market, date, visible position, URL,
and evidence source separately. If no search evidence was collected, mark it
unavailable. Search ranking is not an AI-answer mention or proof of causation.
This worksheet does not require a direct DataForSEO integration.

## 6. Review and report

- [ ] Every observation points to saved evidence and a collection time.
- [ ] Failed and unattempted observations are separate from valid misses.
- [ ] Hit rate denominator includes valid answers only; coverage is disclosed.
- [ ] Measured facts and inferred explanations are labeled separately.
- [ ] Suggestions do not claim causal impact or guaranteed ranking gains.
- [ ] Comparisons use the same prompts and comparable session/market conditions.
- [ ] No measurement, citation, cost, or usage statistic was invented.
- [ ] Private material is kept out of commits and public reports.

Limitations and uncollected evidence: [fill in]

Next steps supported by the observed evidence: [fill in]

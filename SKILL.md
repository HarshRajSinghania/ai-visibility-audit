---
name: ai-visibility-audit
description: >-
  Use when you need to check whether a company, brand, or product is mentioned,
  recommended, or cited in AI answer engines (ChatGPT, Gemini, Google AI Mode,
  Perplexity), plus its Google keyword rankings and competing domains. Produces a
  reproducible, budget-capped audit report with per-question evidence and an
  action list a coding agent can execute.
---
# AI Visibility & SEO Audit

A repeatable procedure for measuring how visible a brand is inside AI-generated
answers and classic search results. It is **provider-agnostic**: any data source
that can (a) ask an AI engine a question and return the answer with cited URLs, and
(b) return keyword rankings / competing domains for a website, will work. If no
paid provider is available, every step has a manual fallback.

Analysis only. This skill never edits the audited website or its code repository.

## 0. Budget and safety

- Ask the caller for a budget before any paid call (suggested default: USD 1).
  Check the provider balance first if the provider exposes one.
- For every endpoint, look up the unit price with a free discovery/inspect call
  first. Skip any endpoint whose price is unknown or exceeds the per-call cap
  (suggested default: USD 0.10).
- Log every call in `raw/cost_ledger.csv` (`endpoint,unit_price_usd,charged,notes`).
  Stop at 95% of budget. Never top up, never add a payment method.
- Asynchronous jobs usually cannot be cancelled once submitted: finalize the
  question list **before** submitting.
- Never put API keys or tokens into the report, raw files, or chat output.

## 1. Define the target

- Brand full name, common aliases / abbreviations, and every public domain
  (main site, secondary sites, marketplace storefronts).
- Using free web access, confirm for each domain: is it online, approximate sitemap
  size, does `robots.txt` allow AI crawlers (e.g. GPTBot, PerplexityBot,
  Google-Extended), is there an `llms.txt`, is there JSON-LD structured data
  (Organization, Product, FAQ).

## 2. AI answer visibility

- Write 5–6 **buying-intent** questions (what a real buyer would ask, without the
  brand name) and 1 **brand** question (asks about the brand directly). The caller
  defines the product scope. For a specific market, run the questions from that
  country's IP / locale if the provider supports it.
- Engines: ChatGPT, Gemini, Google AI Mode, Perplexity — logged-out / default state.
- For every engine × question record:
  - `mentioned` (true/false), `rank` (position in the answer's list, if any),
    `name_used` (how the engine named the brand),
  - `cited_urls` (URLs the answer cited), `competitors` (brands it named),
  - `third_party_sources` (non-brand sites it relied on: directories, reviews,
    marketplaces, forums).
- If a call fails, mark `status: "failed"`. **A failure is not "not mentioned".**
- Manual fallback: ask the same questions in a clean / private browser session of
  each engine and copy the answer and citations.

## 3. Search (SEO) visibility

- For each domain in the target market(s) (e.g. Google US): ranked keywords
  (limit result count to control cost) and competing domains.
- Optional: top-30 SERP for 2–3 core keywords and whether a Google AI Overview
  appears and whom it cites.
- Manual fallback: Google Search Console exports, or a manual SERP check for core
  keywords.

## 4. Output

- Store raw provider responses and `cost_ledger.csv` under `raw/` next to the report.
- Put the structured per-question results in `results.json` (schema: see
  `examples/acme-widgets.results.json`), then optionally render the scorecard with
  `python3 scripts/scorecard.py results.json > scorecard.md`.
- Report (use `templates/report-template.md`), in the caller's language:
  method; per-question table (engine × question); hit-rate summary; competitors;
  keywords; conclusions; an improvement list a coding agent can execute; cost
  ledger. Label every claim **[Measured]** or **[Inferred]**.
- If a previous audit exists, add a "Compared with last audit" section: questions
  that went from not-mentioned to mentioned (and back), rank changes, new
  competitors.

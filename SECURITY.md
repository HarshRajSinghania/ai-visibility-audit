# Security policy

## Supported versions

Security fixes target the latest release. Upgrade before reproducing an issue.

## Reporting a vulnerability

Do not post credentials, private audit results, customer information, or exploit
secrets in a public issue. Use GitHub's **Report a vulnerability** option on the
repository Security tab if it is available. If private reporting is unavailable,
open a minimal issue requesting a private reporting channel without disclosing
vulnerability details or sensitive material. Wait for a private channel before
sharing the reproduction.

A useful private report includes the affected version, impact, a minimal
sanitized reproduction, and a suggested fix if known. No response deadline or
bounty is promised.

## Data handling

Keep real audit files and provider credentials outside the repository. Examples
must use Acme Widgets and `.example` domains. Tests and CI use local fixtures;
they must not call paid APIs or live AI engines. The scorecard reads local JSON
and does not fetch citation URLs or execute answer text.

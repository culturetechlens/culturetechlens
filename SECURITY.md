# Security Policy

CultureTechLens publishes open research data and the scripts that build it.
We take the integrity of the record seriously, including the tools and
pipelines that generate it.

## Reporting a vulnerability

Please do **not** open a public issue for a security problem.

Report privately through either route:

1. GitHub: use **Security → Report a vulnerability** on this repository
   (private vulnerability reporting).
2. Email: info@culturetechlens.com, with "SECURITY" in the subject line.

Include what you found, how to reproduce it, and the files or versions
affected.

## What is in scope

- Code in `tools/` and any build or validation scripts
- Anything that could alter published counts, grades, or record contents
  without a logged change
- Exposed secrets, credentials, or private data in the repository or its
  history

## What is not a security issue

- Factual errors in records. Use the **Report an error** issue form; these
  go to the public corrections log.
- Disagreements about an evidence grade. Open a regular issue with evidence.

## What to expect

We aim to acknowledge security reports within 3 business days and to
provide a status update within 14 days. Fixes are disclosed in the
changelog once they are released.

We will credit reporters in the changelog if they wish, and we ask for a
reasonable period to fix an issue before public disclosure.

## Supported versions

Security fixes apply to the current `main` branch and the most recent
tagged release. Dated snapshots deposited on Zenodo are historical
records and are not modified; where a snapshot is found to contain an
error, an erratum is published instead.

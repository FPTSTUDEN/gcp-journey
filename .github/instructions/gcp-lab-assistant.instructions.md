---
description: "Use when starting, performing, documenting, or wrapping up a Google Cloud Skills Boost lab. Keeps hands-on lab assistance separate from the GCP Lab Atlas catalog and review workflow in GEMINI.md."
---

# Google Cloud Lab Assistant

- Help with the active lab task: explain concepts, guide commands, inspect lab-related evidence, and distinguish attempted actions from verified results.
- Keep this workflow separate from the GCP Lab Atlas. Do not classify labs, update `TAXONOMY.md`, or create or revise atlas records unless explicitly asked.
- For a lab session history, use the `lab-history-record` skill. Record only concise, useful steps and outcomes; redact lab-generated identifiers and never store credentials or tokens.
- At the end of a lab, use the `lab-credential-cleanup` skill to inspect and clean up credentials created specifically for that lab. This instruction authorizes cleanup of clearly lab-specific credentials; do not revoke a personal or shared account, or unrelated Application Default Credentials (ADC).
- Do not make cloud-resource changes or incur costs without clear user authorization. If credential ownership or cleanup scope is uncertain, stop before changing anything and ask one focused question.
- Never claim a command succeeded unless its result was observed or the user reported it. Keep lab instructions and course content summarized in your own words rather than copying them into repository records.

---
name: lab-history-record
description: "Create or update a concise history of a Google Cloud lab session. Use when recording lab commands, progress, observations, outcomes, or troubleshooting; redact lab-generated values and exclude credentials."
---

# Record a lab session

1. Identify the lab folder and its existing `command-history.md`, if present. Use the matching lab folder under `labs/`; do not search unrelated records or change atlas/catalog files as part of this task.
2. Review only the evidence the user provides or the lab-specific files needed to understand it. Separate observed command output from user-reported actions and unverified attempts.
3. Record a concise chronological account of meaningful actions, checks, outcomes, and blockers. Prefer a short description or sanitized command pattern to a raw terminal transcript. Do not copy full lab/course instructions.
4. Redact lab-generated values wherever they appear, including project IDs, account identifiers, resource names and IDs, unique URLs, hostnames, and generated labels. Use clear placeholders such as `[REDACTED_PROJECT_ID]`, `[REDACTED_ACCOUNT]`, or `[REDACTED_RESOURCE_ID]` consistently; retain non-unique technical details only when useful. Partially redact unique links while preserving the scheme, such as replacing `gs://bucket/path` with `gs://[REDACTED_BUCKET_PATH]/path` and `https://host/path` with `https://[REDACTED_API_URL]`.
5. Never write passwords, access tokens, API keys, private keys, credential-file contents, or other secrets into a history record. If supplied evidence contains them, omit them and alert the user that the source should be secured or sanitized.
6. Append to an existing history without rewriting or silently redacting older entries. If no history exists, create `command-history.md` in the identified lab folder. If the target lab or location is ambiguous, ask before creating a file.
7. Report the file updated and summarize what was recorded and redacted. Do not imply that an action succeeded unless the evidence supports it.

## Example

```text
- Created a GKE cluster in [REDACTED_PROJECT_ID] and verified its status was RUNNING.
- Retrieved cluster credentials and confirmed kubectl could reach the cluster.
```

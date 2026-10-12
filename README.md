# GCP Lab Atlas

A lightweight, agent-assisted catalog of Google Cloud Skills Boost labs.

The goal is not to count completed labs. It is to discover which **topics**, **skills**, **services**, and **contexts** each lab exercises, then rank the evidence for those tags consistently.

## Workflow

1. **During the lab:** use the available Gemini assistant with [`prompts/capture-lab.md`](prompts/capture-lab.md). Ask it to classify the lab from the lab instructions and the work you actually performed.
2. **Capture:** save the result as `labs/<short-id>.md`, using [`labs/_template.md`](labs/_template.md).
3. **Separate evidence from inference:** mark anything Gemini inferred but you did not verify as `unverified`.
4. **After the lab:** optionally run Gemini CLI from this repository and ask it to review the record using the `lab-review` skill.
5. **Periodically:** normalize tag names against [`TAXONOMY.md`](TAXONOMY.md), then update the catalog/dashboard.

## Suggested lab filename

`labs/<service>-<short-topic>-<short-context>.md`

Examples:
- `labs/iam-basic-resource-permissions.md`
- `labs/gke-workload-identity.md`
- `labs/gke-debug-workload-access.md`

## Tag groups

- `topic`: underlying concept, e.g. `iam`, `networking`, `observability`
- `skill`: action performed, e.g. `access-control`, `troubleshooting`, `deployment`
- `service`: product/technology, e.g. `gke`, `cloud-iam`, `cloud-storage`
- `context`: larger situation/system, e.g. `cluster-management`, `workload-identity`, `hybrid-cloud`

See `TAXONOMY.md` before inventing a new tag.

## What a tag rank means

Each tag gets a **1–3 evidence rank**, not a universal difficulty score:

- `1 — Exposure`: the lab introduces or walks through the tag.
- `2 — Applied`: you configure, use, inspect, or verify it.
- `3 — Integrated`: you must reason across components, troubleshoot, adapt, or make a design choice involving it.

A rank is assigned per tag, per lab. A single lab can be rank 3 for `deployment` but rank 1 for `iam`. Do not rank based on lab length, number of commands, or how advanced the title sounds.

## Evidence labels

Use one of:
- `guided`: instructions substantially supplied the solution
- `reproduced`: repeated from notes without step-by-step lab guidance
- `adapted`: changed a requirement or configuration and verified the result
- `diagnosed`: investigated a failure and justified the fix
- `designed`: selected and defended an approach for a new scenario

Evidence labels describe what was demonstrated, not a permanent claim of mastery.

## Important boundary

Gemini in the Skills Boost lab environment may not be able to read this repository or its files. In that case, paste the portable prompt from `prompts/capture-lab.md` into the lab's Gemini assistant and copy its output into the repo. `GEMINI.md` and `.gemini/skills/` are for Gemini CLI-compatible repository workflows; they do not automatically configure every Gemini chat surface.

## Start small

For the first 10–20 labs, Markdown records are enough. Do not build a database or complex scoring algorithm until you know which tags and views are genuinely useful.

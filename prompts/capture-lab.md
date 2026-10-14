# Capture and review a lab with Gemini

Act as an autonomous lab-progress analyst. Help me produce a concise, evidence-grounded record for the Google Cloud lab I am working on. Analyze ambitiously, but never turn an inference into a claim that I personally completed or verified an action.

## Autonomous workflow

1. **Understand the lab:** use the title, URL, description, instructions, and repository context available to you. Identify the intended concepts, skills, services, contexts, dependencies, and likely completion signals. Do not reproduce the lab instructions.
2. **Collect available evidence:** when your environment and permissions allow, inspect relevant local artifacts such as terminal history, command output, logs, generated manifests, screenshots, test results, timestamps, and nearby lab notes. Prefer direct evidence over descriptions. Do not access unrelated files, credentials, tokens, private keys, or sensitive project data. If evidence is unavailable, say so.
3. **Ask targeted questions:** ask me how much of the work I actually did, one focused question at a time when needed. Ask about the specific steps that affect the progress conclusion—for example whether I ran a command, adapted a configuration, diagnosed a failure, or only read/followed the instructions. Do not ask me to classify tags manually.
4. **Reconcile evidence:** separate `observed` evidence, my `reported` actions, `inferred` learning value, and `unverified` claims. Resolve contradictions explicitly instead of silently choosing a version.
5. **Conclude progress:** state what I can reasonably record as completed, attempted, partially completed, or not verified. Explain the basis and the remaining gap. Completion of the course page alone is not proof of hands-on completion.
6. **Draft the record:** recommend tags and independent evidence ranks, then show assumptions and judgment calls for my review.

## Tag groups

Use relevant groups only:
- `topic`: underlying concept, e.g. `iam`, `networking`, `observability`
- `skill`: action/capability, e.g. `access-control`, `deployment`, `troubleshooting`
- `service`: product/technology, e.g. `gke`, `cloud-iam`, `cloud-storage`
- `context`: larger system or situation, e.g. `cluster-management`, `workload-identity`, `hybrid-cloud`

For each meaningful tag, recommend a rank:
- `1`: exposure — introduced or followed in a guided flow
- `2`: applied — configured, used, inspected, or verified
- `3`: integrated — adapted, troubleshot, or reasoned across components/trade-offs

Rank what the evidence supports in this lab, not permanent mastery. Do not assign rank 2 or 3 solely because the instructions describe hands-on work. Explain non-obvious ranks, assumptions, and new-tag recommendations.

## Output

Return a concise Markdown record with YAML frontmatter:

---
id: <short-id>
title: "<lab title>"
source_url: "<URL if known>"
completed_on: "<date if known, otherwise blank>"
record_status: draft # draft | reviewed
progress_status: <not-started|in-progress|partial|completed|not-verified>
evidence_summary: <observed|reported|inferred|unverified>
tags:
  topic: []
  skill: []
  service: []
  context: []
---

# Summary

## Progress conclusion
State what is supported, what is only reported, and what remains unverified.

## Evidence collected
List concise evidence items with their source, such as command/output history, log, screenshot, generated file, test result, or user report. Redact secrets and sensitive values.

## Takeaway
Include only if useful.

## Questions or gaps
List only unresolved questions that could change the progress conclusion or ranking.

## My decision / correction
Leave space for me to accept, edit, or reject recommendations.

At the end, briefly list important assumptions, inferred or unverified claims, and non-obvious recommendations. If a question is needed before concluding, ask it instead of pretending the record is final.

Lab details and my notes:
<paste lab title, URL, instructions/description, and anything I noticed or did here>

# Prompt: Capture and classify a Google Cloud lab

You are helping me maintain a personal learning repo. Analyze the lab I am currently doing, using only the lab description/instructions and the actions/results I tell you I actually performed.

Return a concise Markdown lab record with YAML frontmatter. Do not write a tutorial or copy the lab instructions.

Use exactly four tag groups:
- `topic`: underlying concept, e.g. `iam`, `networking`, `observability`
- `skill`: action/capability, e.g. `access-control`, `deployment`, `troubleshooting`
- `service`: product/technology, e.g. `gke`, `cloud-iam`, `cloud-storage`
- `context`: larger situation/system, e.g. `cluster-management`, `workload-identity`, `hybrid-cloud`

For each tag, include:
- `name`
- `rank`: 1, 2, or 3
- `confidence`: high, medium, or low
- `evidence`: one short reason grounded in the material

Rank tags independently:
1 = exposure: introduced or followed in a guided procedure
2 = applied: configured, used, inspected, or verified hands-on
3 = integrated: adapted, troubleshot, or reasoned across components/trade-offs

Rules:
- Do not rank based on lab length, number of commands, or title.
- Do not claim I performed an action unless I say I did.
- Distinguish the task described by the lab from evidence of what I personally did.
- Prefer existing common tags and lowercase kebab-case.
- Flag new tag suggestions separately under `Candidate tags`; do not treat them as established taxonomy.
- If something is uncertain, mark it unverified rather than guessing.
- Keep the record short.

Use this output shape:

---
id: <short-stable-id>
title: "<lab title>"
source_url: "<URL if available>"
completed_on: "<YYYY-MM-DD or blank>"
status: <in-progress|completed|review-needed>
evidence_type: <guided|reproduced|adapted|diagnosed|designed>
tags:
  topic: [...]
  skill: [...]
  service: [...]
  context: [...]
---

# Summary
# What I actually did
# Evidence
# Takeaway
# Open question

At the end, provide a short `Candidate tags` section only if needed.

I will now provide the lab title, instructions or description, and what I actually did:

# Capture a lab with Gemini

Help me make a concise progress record for the Google Cloud lab I am working on. Treat this as a first draft that I can edit, not a form that must be filled perfectly.

Use the lab title, description/instructions, and any notes I provide. Analyze ambitiously: infer likely learning goals, meaningful relationships, relevant tags, and evidence-rank recommendations. Make useful recommendations instead of asking me to classify everything myself.

Use these tag groups where relevant:
- `topic`: underlying concept, e.g. `iam`, `networking`, `observability`
- `skill`: action/capability, e.g. `access-control`, `deployment`, `troubleshooting`
- `service`: product/technology, e.g. `gke`, `cloud-iam`, `cloud-storage`
- `context`: larger system or situation, e.g. `cluster-management`, `workload-identity`, `hybrid-cloud`

For each meaningful tag, recommend a rank:
- `1`: exposure — introduced or followed in a guided flow
- `2`: applied — configured, used, inspected, or verified
- `3`: integrated — adapted, troubleshot, or reasoned across components/trade-offs

Keep the record short and proportional to the lab. Empty tag groups and omitted sections are fine. Use existing tags when they fit, but suggest a new tag if it captures a useful distinction. Briefly explain non-obvious rankings, assumptions, and uncertain classifications so I can exercise judgment.

Important: distinguish what the lab is designed to teach, what I reported doing, what I directly verified, and what you inferred. Be conservative about personal claims: do not claim I performed, completed, or verified actions unless I told you so. You can still draft an ambitious analysis from the lab description; mark recommendations and uncertain details as inferred or unverified rather than stopping to ask questions. Do not copy the lab instructions verbatim.

Return a Markdown record with YAML frontmatter, following this loose shape:

---
id: <short-id>
title: "<lab title>"
source_url: "<URL if known>"
completed_on: "<date if known, otherwise blank>"
record_status: draft
tags:
  topic: []
  skill: []
  service: []
  context: []
---

# Summary
# Takeaway (if useful)
# Evidence or notes (if available)
# My decision / correction (leave for me to edit)

At the end, briefly list important assumptions, inferred or unverified claims, non-obvious recommendations, and any new tag suggestion. Do not add a long evaluation essay.

Lab details and my notes:
<paste lab title, URL, instructions/description, and anything I noticed or did here>

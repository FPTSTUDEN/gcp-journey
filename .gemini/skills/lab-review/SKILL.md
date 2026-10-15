---
name: lab-review
description: Review a GCP lab record, collect available evidence, ask focused progress questions, and conclude what the record supports.
---

# Review a lab record

1. Read `TAXONOMY.md`, `GEMINI.md`, and the target lab record.
2. Proactively inspect the target record and nearby, clearly related repository artifacts before asking the user to recount their work. Inspect other relevant outputs, logs, manifests, screenshots, test results, or timestamps only when their location is known and access is permitted. Use read-only inspection; do not broadly search the filesystem or shell history, assume access outside the repository or current conversation, or run commands that change cloud resources. Do not access unrelated files, credentials, tokens, private keys, or sensitive project data.
3. Report which evidence sources you inspected and what each establishes. Note important evidence sources that were unavailable; do not treat unavailable evidence as proof either way. Redact secrets and sensitive values.
4. Separate evidence provenance: `observed` means directly inspected, `reported` means the user stated it, `inferred` means AI analysis, and `unverified` means not sufficiently supported. Evidence of an attempt does not by itself prove a successful result.
5. Ask one focused question only when the evidence leaves a meaningful uncertainty about progress or ranking. Do not ask the learner to classify tags manually.
6. Conclude progress explicitly as not-started, in-progress, partial, completed, or not-verified. Completion claims require supporting evidence; a lab description or course completion indicator alone is insufficient.
7. Check whether tags communicate useful distinctions across topic, skill, service, and context. Do not insist that every group be populated.
8. Be ambitious in analysis: identify meaningful concepts, relationships, likely learning value, and useful tag distinctions from the material.
9. Recommend per-tag evidence ranks from 1–3. Do not assign applied or integrated ranks solely from instructions; base them on observed or reported work and label the basis.
10. Make assumptions, recommendations, contradictions, and remaining gaps visible. The user owns final interpretations and can accept, edit, or reject them.
11. Do not infer that the learner personally performed a task just because the lab describes it.

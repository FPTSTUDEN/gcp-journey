# GCP Lab Atlas — Gemini instructions

You help maintain a structured catalog of Google Cloud learning labs.

## Source of truth
- Read `TAXONOMY.md` before proposing or editing tags.
- Use `labs/_template.md` as the record format.
- Preserve user-provided evidence and URLs.
- Never invent lab steps, outcomes, screenshots, commands run, or completion status.

## Classification
For every lab, classify meaningful tags into exactly these groups:
- `topic`: underlying concept
- `skill`: action/capability exercised
- `service`: product/technology
- `context`: larger system or situation

Use existing taxonomy tags when possible. Propose new tags separately as candidates with a short justification; do not silently add synonyms.

## Rank each tag independently
Use rank 1–3:
1. Exposure — introduced or followed in a guided flow.
2. Applied — configured, used, inspected, or verified.
3. Integrated — adapted, troubleshot, or reasoned across components or trade-offs.

Rank based on the demonstrated task and evidence, not the lab's length, title, or number of commands. Do not confuse a lab's apparent complexity with the learner's independence.

## Evidence discipline
Distinguish:
- what the lab instructions ask for,
- what the learner says they actually did,
- what is directly verified,
- what remains inferred or unverified.

If evidence is missing, use `unknown` or `unverified`; ask one concise follow-up only if necessary. Do not claim mastery from completion alone.

## Editing discipline
- Keep lab records concise.
- Do not duplicate full lab instructions or copyrighted course content.
- Do not store credentials, access tokens, private keys, or sensitive project data.
- Update generated catalog files only when explicitly asked or when the repository workflow calls for it.
- When reviewing existing records, explain any tag/rank changes briefly.

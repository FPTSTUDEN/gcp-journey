# Tag taxonomy

Use these four groups. Tags are reusable labels; do not nest a tag under another tag just because one often appears in that context.

## `topic` — What concept is involved?

Examples:
- `iam`
- `networking`
- `compute`
- `containers`
- `observability`
- `data-storage`
- `deployment-automation`
- `secrets-management`

## `skill` — What action or capability is exercised?

Examples:
- `access-control`
- `identity-configuration`
- `deployment`
- `configuration`
- `monitoring`
- `troubleshooting`
- `debugging`
- `automation`
- `architecture-design`
- `cost-optimization`

Prefer verbs or action-oriented nouns. `kubernetes` is a service, not a skill. `troubleshooting` is a skill, not a topic.

## `service` — Which product or technology is used?

Examples:
- `gke`
- `cloud-iam`
- `cloud-storage`
- `cloud-logging`
- `cloud-monitoring`
- `cloud-build`
- `compute-engine`
- `vpc-networking`

Use the most specific service that is genuinely relevant. Avoid tagging every Google Cloud product merely mentioned in the lab.

## `context` — In what larger system or situation is it applied?

Examples:
- `resource-permissions`
- `cluster-management`
- `workload-identity`
- `runtime-access`
- `network-connectivity`
- `ci-cd-pipeline`
- `hybrid-cloud`
- `production-security`
- `incident-response`

Context describes the setting/problem, not a parent folder. A lab may have several contexts.

## Tagging rules

1. Add a tag only when the lab meaningfully exercises it. Mentioning a service in passing is not enough.
2. Use lowercase kebab-case.
3. Reuse existing tags before creating new ones.
4. Keep `topic`, `skill`, `service`, and `context` semantically distinct.
5. It is fine for one lab to have multiple tags in one group.
6. If uncertain, propose a tag with `status: candidate` rather than silently expanding the taxonomy.
7. Rank every tag separately. Do not give all tags the same rank just because they belong to one lab.

## Tag evidence rank (1–3)

- `1 — exposure`: introduced, explained, or followed in a guided procedure.
- `2 — applied`: configured, used, inspected, or verified hands-on.
- `3 — integrated`: adapted, diagnosed, compared, or reasoned across components/trade-offs.

Rank what the learner actually did. If the lab only shows a command but the learner did not run or inspect it, do not claim hands-on evidence.

## Confidence

- `high`: directly supported by lab tasks and observed actions
- `medium`: strongly implied by the task, but evidence is incomplete
- `low`: inferred from title or description only

Low-confidence tags should be reviewed or removed.

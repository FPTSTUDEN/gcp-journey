# Tag taxonomy

This is a shared vocabulary for the lab map, not a rigid schema. Reuse tags where sensible, but propose new ones when they describe something meaningfully different.

## `topic` — What concept is involved?
Examples: `iam`, `networking`, `compute`, `containers`, `observability`, `data-storage`, `deployment-automation`, `secrets-management`.

## `skill` — What action or capability is exercised?
Examples: `access-control`, `identity-configuration`, `deployment`, `configuration`, `monitoring`, `troubleshooting`, `debugging`, `automation`, `architecture-design`, `cost-optimization`.

## `service` — Which product or technology is used?
Examples: `gke`, `cloud-iam`, `cloud-storage`, `cloud-logging`, `cloud-monitoring`, `cloud-build`, `compute-engine`, `vpc-networking`.

## `context` — In what larger system or situation is it applied?
Examples: `resource-permissions`, `cluster-management`, `workload-identity`, `runtime-access`, `network-connectivity`, `ci-cd-pipeline`, `hybrid-cloud`, `production-security`, `incident-response`.

## Practical tagging guidance
- Tag what the lab meaningfully exercises, not every service it mentions.
- Use lowercase kebab-case for consistency.
- Tags should have distinct meanings: `iam` is a topic; `troubleshooting` is a skill; `gke` is a service; `workload-identity` is a context.
- A lab can have multiple tags in any group, or none in a group if that group adds little.
- These examples are a starting point. Gemini may suggest new tags or alternatives; the user decides whether to adopt them.

## Evidence rank (per tag, per lab)
Use a simple 1–3 recommendation:
- `1 — Exposure`: introduced or followed in a guided flow.
- `2 — Applied`: configured, used, inspected, or verified.
- `3 — Integrated`: adapted, troubleshot, or reasoned across components or trade-offs.

Rank the evidence for each tag separately. A lab might provide rank 3 evidence for `deployment` and rank 1 for `iam`. The rank is not a universal difficulty score or a claim of lasting mastery. Use judgment and briefly explain ambiguous calls; don't measure by lab length or command count.

# GCP Lab Atlas

An AI-assisted catalog of Google Cloud Skills Boost labs. Gemini analyzes ambitiously—surfacing concepts, relationships, learning value, and tag recommendations—while remaining conservative about personal claims. You retain the final say over the tags and what they mean.

## Workflow

1. **During or after a lab:** use Gemini with [`prompts/capture-lab.md`](prompts/capture-lab.md). Give it the lab title/description and any observations you have. It should first inspect relevant repository evidence that is available and permitted, report what it checked, and ask only about meaningful remaining gaps. Evidence gathering is read-only and does not include broad searches, credentials, or cloud-side actions.
2. **Capture:** save its draft in `labs/<short-id>.md`. You can keep it rough; not every section needs content.
3. **Review lightly:** correct anything that feels wrong, especially meaningful tag or rank decisions. Set `record_status: reviewed` when you're happy with it. You do not need to manually verify every obvious suggestion.
4. **Periodically:** ask Gemini CLI to find patterns, suggest taxonomy improvements, and refresh catalog views.

## Four tag groups

- `topic`: underlying concept, e.g. `iam`, `networking`
- `skill`: action/capability, e.g. `access-control`, `troubleshooting`
- `service`: product/technology, e.g. `gke`, `cloud-storage`
- `context`: larger system/situation, e.g. `cluster-management`, `workload-identity`

See [`TAXONOMY.md`](TAXONOMY.md). It's a shared vocabulary, not a rigid list.

## Per-tag evidence rank

- `1 — Exposure`: introduced or followed in a guided flow
- `2 — Applied`: configured, used, inspected, or verified
- `3 — Integrated`: adapted, troubleshot, or reasoned across components/trade-offs

The rank describes evidence in that lab, not permanent mastery. A lab can rank differently for different tags.

## Human ownership

AI should be ambitious in analysis and transparent about recommendations, assumptions, and uncertainty. It must not treat a lab description or its own inference as proof that you performed or verified an action. You decide which tags and interpretations are useful, correct, or worth keeping. Records may remain drafts; `reviewed` simply means you have looked over the meaningful decisions, not that every detail is perfect.

## Gemini surfaces

The Gemini assistant inside Skills Boost may not have access to repository files. Paste the capture prompt there and copy the result into the repo. `GEMINI.md` and `.gemini/skills/` are for compatible repository workflows such as Gemini CLI.

## Keep it lightweight

Start with Markdown. Add scripts or elaborate scoring only when repeated use shows a real need.

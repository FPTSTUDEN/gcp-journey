---
name: catalog-maintenance
description: Normalize lab tags, detect duplicate labels, and update the GCP lab catalog and progress views from existing Markdown records.
---

# Maintain the catalog

1. Read `TAXONOMY.md` and `GEMINI.md`.
2. Scan lab records in `labs/`.
3. Report unknown tags, near-duplicate tags, missing tag groups, malformed ranks, and records with low-confidence classifications.
4. Do not silently rename tags across many files. Propose a mapping first, such as `gke-iam` -> `workload-identity`.
5. When asked to update indexes, derive counts from lab records; do not manually invent totals.
6. Separate:
   - number of labs mentioning a tag,
   - highest evidence rank observed for that tag,
   - number of distinct contexts in which the tag appears.
7. Do not interpret the highest rank as proof of permanent mastery. Describe it as the strongest recorded evidence.
8. Keep generated views reproducible and avoid editing lab records unless explicitly requested.

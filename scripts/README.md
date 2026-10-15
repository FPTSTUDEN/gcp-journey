# Scripts

## Create a lab record

Run `python scripts/create_lab.py` from the repository root. Enter the lab name, then enter the description one line at a time. Type `END` on its own line to finish the description. The script creates `labs/<slug>/lab.md` from [`labs/_template.md`](../labs/_template.md), plus appendable proof files: `command-history.md` for commands and outputs, and `observations.md` for manual observations and verification notes. It refuses to overwrite an existing lab folder. Redact secrets before adding evidence.

Useful future automation:
- validate YAML frontmatter and rank values
- detect tags absent from `TAXONOMY.md`
- generate tag frequency/rank summaries
- render a Mermaid graph or Markdown matrix

Avoid making a custom application before the taxonomy has survived a few dozen labs.

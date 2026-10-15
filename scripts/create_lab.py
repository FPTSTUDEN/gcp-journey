"""Create a new lab record from the shared template."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LABS_DIR = ROOT / "labs"
TEMPLATE_PATH = LABS_DIR / "_template.md"
DESCRIPTION_END_MARKER = "END"
PROOF_FILES = {
    "command-history.md": "# Command history\n\nAppend commands and their relevant outputs here. Redact secrets before saving.\n",
    "observations.md": "# Observations\n\nAppend manual observations, screenshots, and verification notes here.\n",
}


def slugify(title: str) -> str:
    """Turn a lab title into a stable, lowercase folder name."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if not slug:
        raise ValueError("The lab name must contain at least one letter or number.")
    return slug


def read_description() -> str:
    """Read a possibly multiline description until the end marker is entered."""
    print(
        f"Enter the description. Type {DESCRIPTION_END_MARKER} on its own line when finished."
    )
    lines: list[str] = []
    for line in sys.stdin:
        line = line.rstrip("\r\n")
        if line == DESCRIPTION_END_MARKER:
            break
        lines.append(line)
    else:
        raise ValueError(
            f"Description must end with {DESCRIPTION_END_MARKER} on its own line."
        )

    description = "\n".join(lines).strip()
    if not description:
        raise ValueError("The description cannot be empty.")
    return description


def create_lab(title: str, description: str) -> Path:
    """Create a lab folder and render its Markdown record."""
    folder = LABS_DIR / slugify(title)
    if folder.exists():
        raise FileExistsError(f"A lab folder already exists: {folder}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = template.replace("id: short-stable-id", f"id: {folder.name}", 1)
    content = content.replace('title: "Lab title"', f'title: "{title}"', 1)
    content = content.replace("One or two sentences in your own words.", description, 1)

    folder.mkdir()
    with (folder / "lab.md").open("w", encoding="utf-8", newline="\n") as lab_file:
        lab_file.write(content)
    for filename, initial_content in PROOF_FILES.items():
        with (folder / filename).open("w", encoding="utf-8", newline="\n") as proof_file:
            proof_file.write(initial_content)
    return folder


def main() -> int:
    print("Create a new GCP lab record")
    title = input("Lab name: ").strip()
    if not title:
        print("Error: the lab name cannot be empty.", file=sys.stderr)
        return 1

    try:
        folder = create_lab(title, read_description())
    except (FileExistsError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Created {folder.relative_to(ROOT)}\\lab.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

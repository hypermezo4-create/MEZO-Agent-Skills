from __future__ import annotations

from validation.common import ROOT, markdown_links


def validate_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for link in markdown_links(text):
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            destination = (markdown.parent / link.split("#", 1)[0]).resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{markdown.relative_to(ROOT)}: link escapes repository: {link}")
                continue
            if not destination.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: broken link: {link}")
    return errors

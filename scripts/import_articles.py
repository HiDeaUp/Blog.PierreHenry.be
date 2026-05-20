#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
import unicodedata
from collections import Counter
from pathlib import Path


DEFAULT_SOURCE = Path.home() / "Code" / "youtube-to-medium-blog-posts-automation" / "articles"
DEFAULT_TARGET = Path(__file__).resolve().parent.parent / "content" / "blog"

ENGLISH_MARKERS = {
    "the", "and", "you", "your", "with", "that", "this", "from", "for", "are",
    "have", "will", "more", "than", "when", "what", "work", "time", "life", "can",
    "focus", "build", "better", "engineer", "software", "travel", "money", "productivity",
    "habit", "habits", "project", "projects", "business", "future", "today", "people",
    "great", "simple", "learn", "using", "without", "start", "stop", "into", "want",
}

FRENCH_MARKERS = {
    "que", "pour", "avec", "dans", "une", "des", "est", "pas", "plus", "comment",
    "faire", "tout", "bien", "vie", "temps", "sur", "les", "ton", "ta", "ses",
    "pourquoi", "réussir", "grâce", "mieux", "jour", "jours", "être", "comme", "par",
    "sans", "encore", "cela", "quand", "nous", "vous", "mon", "tes", "leurs", "avoir",
}

PRIORITY_TOPICS = {
    "tech": {
        "software engineering", "software engineer", "developer", "developers", "coding", "code",
        "programming", "ai", "copilot", "cursor", "mcp", "claude", "chatgpt", "react",
        "python", "terminal", "repository", "codebase", "data science", "electron",
    },
    "nomad": {
        "travel", "travelling", "traveling", "nomad", "digital nomad", "remote work", "remote",
        "location independence", "expat", "airport", "backpack", "kuala lumpur", "thailand", "vietnam",
    },
    "money": {
        "money", "salary", "pay", "negotiation", "income", "freelance", "freelancer", "revenue",
        "pricing", "finance", "financial", "invest", "investing", "rich", "wealth", "bonus",
        "contract", "equity", "stock options", "esop", "isop",
    },
    "wealth": {
        "wealth", "rich", "invest", "investing", "assets", "capital", "financial freedom",
        "net worth", "lifestyle inflation",
    },
    "time management": {
        "time management", "schedule", "scheduling", "calendar", "plan your week", "weekly plan",
        "daily plan", "priorities", "priority", "organize", "organise", "planning",
    },
    "tasks": {
        "tasks", "task", "to-do", "todo", "checklist", "execute", "execution", "finish what you start",
    },
    "productivity": {
        "productivity", "focus", "deep work", "pomodoro", "efficiency", "efficient", "organize",
        "workflow", "workload", "system", "systems",
    },
    "time blocking": {
        "time blocking", "time boxing", "timeboxing", "time-boxing", "time-blocking",
    },
    "entrepreneurship": {
        "entrepreneur", "entrepreneurship", "solopreneur", "startup", "saas", "business", "audience",
        "offer", "freelance", "brand", "side business", "side hustle",
    },
}

HEADING_REPLACEMENTS = {
    "tl;dr / key takeaways": "## Key Takeaways",
    "key takeaways": "## Key Takeaways",
    "actions list": "## Action Steps",
    "ask yourself": "## Reflection",
}

PROMO_MARKERS = {
    "book.ph7.me",
    "podcasts.ph7.me",
    "masterclass.ph7.me",
    "ko-fi.com/phenry",
    "retainr.io",
    "subscribe to my youtube channel",
    "support my work with a coffee",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import English markdown articles into Hugo blog posts.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Source article directory")
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET, help="Target Hugo content/blog directory")
    parser.add_argument("--clean", action="store_true", help="Delete previously generated blog posts before importing")
    return parser.parse_args()


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    raw_front_matter = parts[0].removeprefix("---\n")
    body = parts[1]
    data: dict[str, str] = {}
    for raw_line in raw_front_matter.splitlines():
        if not raw_line.strip() or ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    return cleaned or "article"


def escape_toml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z']+", text.lower())


def normalize_keyword_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def looks_english(path: Path, metadata: dict[str, str], body: str) -> bool:
    if "fr" in path.parts:
        return False

    sample = " ".join(
        [
            metadata.get("optimized_title", ""),
            metadata.get("tags", ""),
            body[:4000],
        ]
    )
    tokens = tokenize(sample)
    if len(tokens) < 80:
        return False

    english_hits = sum(token in ENGLISH_MARKERS for token in tokens)
    french_hits = sum(token in FRENCH_MARKERS for token in tokens)
    accent_hits = len(re.findall(r"[àâçéèêëîïôùûüÿœ]", sample.lower()))

    if english_hits < 16:
        return False
    if french_hits > english_hits:
        return False
    if accent_hits > english_hits:
        return False

    return True


def split_tags(raw_tags: str) -> list[str]:
    tags = [tag.strip().lower() for tag in raw_tags.split(",") if tag.strip()]
    seen: set[str] = set()
    unique_tags: list[str] = []
    for tag in tags:
        if tag not in seen:
            unique_tags.append(tag)
            seen.add(tag)
    return unique_tags


def detect_priority_topics(title: str, tags: list[str], body: str) -> list[str]:
    haystack = normalize_keyword_text(" ".join([title, " ".join(tags), body[:4000]]))
    topics: list[str] = []
    for topic, keywords in PRIORITY_TOPICS.items():
        if any(normalize_keyword_text(keyword) and f" {normalize_keyword_text(keyword)} " in f" {haystack} " for keyword in keywords):
            topics.append(topic)
    return topics


def strip_leading_heading_block(body: str) -> str:
    lines = body.splitlines()
    kept_prefix: list[str] = []
    index = 0

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            kept_prefix.append(lines[index])
            index += 1
            continue
        if stripped.startswith("!["):
            kept_prefix.append(lines[index])
            index += 1
            continue
        if kept_prefix and stripped.startswith("*") and stripped.endswith("*"):
            kept_prefix.append(lines[index])
            index += 1
            continue
        break

    heading_index = index
    saw_heading = False
    checked_non_empty = 0
    while heading_index < len(lines) and checked_non_empty < 8:
        stripped = lines[heading_index].strip()
        if not stripped:
            heading_index += 1
            continue
        checked_non_empty += 1
        if stripped.startswith("#"):
            saw_heading = True
            heading_index += 1
            continue
        break

    if saw_heading:
        trimmed = kept_prefix + ([""] if kept_prefix else []) + lines[heading_index:]
        return "\n".join(trimmed).strip()
    return body.strip()


def normalize_sections(body: str) -> str:
    normalized_lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        heading_match = re.match(r"^#{1,6}\s+\*?(.*?)\*?$", stripped)
        if heading_match:
            label = heading_match.group(1).strip().lower()
            replacement = HEADING_REPLACEMENTS.get(label)
            if replacement:
                normalized_lines.append(replacement)
                continue
        normalized_lines.append(line)

    text = "\n".join(normalized_lines)
    text = re.sub(r"(?m)^https://(?:www\.)?youtube\.com/watch\?v=.*$\n?", "", text)
    text = re.sub(r"(?m)^https://youtu\.be/.*$\n?", "", text)
    text = re.sub(r"(?m)^(👋|📺|⚡️).*\n?", "", text)
    text = re.sub(r"(?mi)^and \[retainr\.io\].*\n?", "", text)
    text = re.sub(r"\n(?:---\s*\n){2,}", "\n---\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    kept_chunks: list[str] = []
    saw_prose = False
    for chunk in re.split(r"\n\s*\n", text):
        stripped_chunk = chunk.strip()
        lowered_chunk = stripped_chunk.lower()
        if stripped_chunk == "---" and not saw_prose:
            continue
        if stripped_chunk and any(marker in lowered_chunk for marker in PROMO_MARKERS):
            continue
        if stripped_chunk and stripped_chunk != "---" and not stripped_chunk.startswith("!["):
            if not (stripped_chunk.startswith("*") and stripped_chunk.endswith("*")):
                saw_prose = True
        kept_chunks.append(stripped_chunk)

    text = "\n\n".join(chunk for chunk in kept_chunks if chunk)
    text = re.sub(r"\A(?:---\s*)+", "", text)
    text = re.sub(r"(?:\s*---)+\s*\Z", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[`*_>#-]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_summary(body: str) -> str:
    for chunk in re.split(r"\n\s*\n", body):
        stripped = chunk.strip()
        if not stripped:
            continue
        if stripped.startswith(("![", "#", "*")):
            continue
        if stripped == "---":
            continue
        summary = strip_markdown(stripped)
        if len(summary) >= 40:
            return summary[:197].rstrip() + ("..." if len(summary) > 197 else "")
    return ""


def normalize_body(body: str) -> str:
    cleaned = strip_leading_heading_block(body)
    cleaned = normalize_sections(cleaned)
    return cleaned.strip() + "\n"


def render_front_matter(metadata: dict[str, str], title: str, slug: str, tags: list[str], summary: str, priority_topics: list[str]) -> str:
    lines = [
        "+++",
        f'title = "{escape_toml(title)}"',
        f'slug = "{escape_toml(slug)}"',
        f'date = "{escape_toml(metadata.get("date", "1970-01-01T00:00:00"))}"',
        "draft = false",
    ]

    if summary:
        lines.append(f'description = "{escape_toml(summary)}"')
        lines.append(f'summary = "{escape_toml(summary)}"')

    if tags:
        rendered_tags = ", ".join(f'"{escape_toml(tag)}"' for tag in tags)
        lines.append(f"tags = [{rendered_tags}]")

    if priority_topics:
        lines.append("priority = true")
        rendered_topics = ", ".join(f'"{escape_toml(topic)}"' for topic in priority_topics)
        lines.append(f"priority_topics = [{rendered_topics}]")

    original_title = metadata.get("original_title")
    if original_title:
        lines.append(f'original_title = "{escape_toml(original_title)}"')

    medium_url = metadata.get("medium_url")
    if medium_url:
        lines.append(f'source_medium = "{escape_toml(medium_url)}"')

    youtube_url = metadata.get("youtube_url")
    if youtube_url:
        lines.append(f'source_youtube = "{escape_toml(youtube_url)}"')

    lines.append("+++")
    return "\n".join(lines)


def ensure_clean_target(target: Path) -> None:
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)
        return
    for child in target.glob("*.md"):
        if child.name.startswith("_"):
            continue
        child.unlink()


def import_articles(source: Path, target: Path, clean: bool) -> None:
    if clean:
        ensure_clean_target(target)
    else:
        target.mkdir(parents=True, exist_ok=True)

    imported = 0
    skipped = 0
    priority_count = 0
    topic_counter: Counter[str] = Counter()
    slug_counter: Counter[str] = Counter()

    for path in sorted(source.rglob("*.md")):
        if path.name == ".gitkeep":
            continue

        text = path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)

        if not metadata.get("optimized_title") or not looks_english(path, metadata, body):
            skipped += 1
            continue

        title = metadata["optimized_title"].strip()
        cleaned_body = normalize_body(body)
        summary = extract_summary(cleaned_body)
        tags = split_tags(metadata.get("tags", ""))
        priority_topics = detect_priority_topics(title, tags, cleaned_body)
        for topic in priority_topics:
            if topic not in tags:
                tags.append(topic)
        tags = sorted(dict.fromkeys(tags))

        slug = slugify(title)
        slug_counter[slug] += 1
        if slug_counter[slug] > 1:
            slug = f"{slug}-{slug_counter[slug]}"

        front_matter = render_front_matter(metadata, title, slug, tags, summary, priority_topics)
        destination = target / f"{slug}.md"
        destination.write_text(f"{front_matter}\n\n{cleaned_body}", encoding="utf-8")

        imported += 1
        if priority_topics:
            priority_count += 1
            topic_counter.update(priority_topics)

    print(f"Imported {imported} English articles into {target}")
    print(f"Skipped {skipped} files that were non-English, incomplete, or intentionally excluded")
    print(f"Priority articles: {priority_count}")
    if topic_counter:
        print("Priority topic counts:")
        for topic, count in topic_counter.most_common():
            print(f"  - {topic}: {count}")


def main() -> None:
    args = parse_args()
    import_articles(args.source.resolve(), args.target.resolve(), args.clean)


if __name__ == "__main__":
    main()

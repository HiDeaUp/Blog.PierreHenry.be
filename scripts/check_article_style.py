#!/usr/bin/env python3
"""Check article wording and image markup."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "content" / "blog"

PHRASE_REPLACEMENTS = {
    "one must consider": "consider",
    "transformative experience": "meaningful experience",
    "let's dive in": "here is how",
    "let’s dive in": "here is how",
    "let's dive": "here is how",
    "let’s dive": "here is how",
    "cutting-edge technology": "current technology",
    "cutting edge technology": "current technology",
    "digital age": "online world",
    "fast-paced": "busy",
    "fast paced": "busy",
    "game-changer": "major improvement",
    "game changer": "major improvement",
    "the possibilities are endless": "there are many possibilities",
    "possibilities are endless": "many options are available",
    "the there are many possibilities": "there are many possibilities",
    "endless possibilities": "many possibilities",
    "endless opportunities": "many opportunities",
    "endless distractions": "many distractions",
    "endless list": "long list",
    "endless cycle": "repeating cycle",
    "endless stream": "constant stream",
    "endless to-do lists": "long to-do lists",
    "endless notes": "too many notes",
    "endless research": "too much research",
    "endless buying": "compulsive buying",
    "endless thrills": "new thrills",
    "endless goals": "too many goals",
    "endless progress": "more progress",
    "constant buying": "compulsive buying",
    "constant progress": "more progress",
    "endless repetition": "repeated drills",
    "ticking off endless tasks": "ticking off task after task",
    "endless tasks": "too many tasks",
    "endless questions": "too many questions",
    "endless options": "too many options",
    "endless complaints": "repeated complaints",
    "endless scrolling": "compulsive scrolling",
    "endless rumination": "repeated rumination",
    "endless learning": "passive learning",
    "endless workdays": "long workdays",
    "endless preparation": "too much preparation",
    "endless procrastination": "continued procrastination",
    "endless comparison": "constant comparison",
    "endless notifications": "constant notifications",
    "endless pings": "constant pings",
    "endless temptations": "many temptations",
    "endless links": "too many links",
    "endless to-dos": "too many to-dos",
    "endless hours": "long hours",
    "endless time": "unlimited time",
    "endless marathons": "long marathons",
    "endless coffee shops": "many coffee shops",
    "endless personal possibilities": "many personal possibilities",
    "endless loop": "repeating loop",
    "endless search": "constant search",
    "endless planning": "too much planning",
    "endless consumption": "passive consumption",
    "endless examples": "many examples",
    "endless diplomas": "many diplomas",
    "your day isn’t endless": "your day is limited",
    "your day isn't endless": "your day is limited",
    "the day isn’t endless": "the day is limited",
    "the day isn't endless": "the day is limited",
    "life is endless": "life will last forever",
    "the tunnel seems endless": "the tunnel seems to have no end",
    "days felt endless": "days dragged on",
    "work felt endless": "work dragged on",
    "searching endlessly": "searching over and over",
    "endlessly searching": "searching over and over",
    "endlessly reflecting": "reflecting for too long",
    "endlessly planning": "planning for too long",
    "get back in shape": "get fit",
    "stay in shape": "stay fit",
    "in good shape": "in good condition",
    "in top shape": "in good condition",
    "in great shape": "in great condition",
    "embracing your passions shapes": "following your passions builds",
    "specialization and consistency shape your unique expertise": "specialization and consistency build your unique expertise",
    "habits quietly shape your happiness": "habits quietly affect your happiness",
    "how to shape your mood": "how to change your mood",
    "how to shape your space": "how to arrange your space",
    "how to shape your day": "how to plan your day",
    "how to shape your future": "how to build your future",
    "how to shape your mind": "how to train your mind",
    "how to shape your environment": "how to change your environment",
    "how to shape your success": "how to build your success",
    "how to shape your": "how to build your",
    "how to shape a": "how to build a",
    "shape your mood": "change your mood",
    "shape your space": "arrange your space",
    "shape your day": "plan your day",
    "shape your future": "build your future",
    "shape your mind": "train your mind",
    "shape your happiness": "build your happiness",
    "shape your attitude": "change your attitude",
    "shape your ideal lifestyle": "design your ideal lifestyle",
    "shape your ideal week": "design your ideal week",
    "shape your ideal month": "design your ideal month",
    "shape your ideal life": "design your ideal life",
    "shape your days around": "organize your days around",
    "shape your days to": "plan your days to",
    "shape your own definition": "define yourself",
    "shape the life you": "build the life you",
    "shape the life i": "build the life I",
    "shape your story": "write your story",
    "shape your reality": "change your reality",
    "shape your perception": "change your perception",
    "shape your surroundings": "arrange your surroundings",
    "shape your own path": "choose your own path",
    "shape your path": "choose your path",
    "shape your tomorrow": "build your tomorrow",
    "shape my future": "build my future",
    "shape your dream life": "build your dream life",
    "shape your life to match your dreams": "build a life that matches your dreams",
    "shape your days according to": "plan your days around",
    "shape each day to make": "plan each day to make",
    "shaping each day": "planning each day",
    "shaping my days": "planning my days",
    "shaping your days": "planning your days",
    "shaping a life": "building a life",
    "create and shape things": "create things",
    "molds us into a certain shape": "influences us in certain ways",
    "progress take shape": "progress become visible",
    "take shape": "become real",
    "changes shape": "looks different",
    "shape and location": "form and location",
    "shape a fulfilling life": "build a fulfilling life",
    "alternating opposites shapes": "alternating opposites affect",
    "v shape": "V posture",
    "rounded shapes": "rounded forms",
    "soft shapes": "soft forms",
    "these shapes": "these forms",
    "the shapes": "the forms",
    "shapes and colors": "forms and colors",
    "shapes, colors": "forms, colors",
    "shape your": "influence your",
    "shape our": "influence our",
    "shape the": "influence the",
    "shape a life": "build a life",
    "shape success": "build success",
    "shape happiness": "build happiness",
    "shaping adventures": "planning adventures",
    "the shape of": "the form of",
    "a shape": "a form",
    "sharp-edged": "hard-edged",
    "sharp, square edges": "hard, square edges",
    "sharp objects": "pointed objects",
    "sharp corners": "pointed corners",
    "sharp corner": "pointed corner",
    "sharp angles": "pointed angles",
    "sharp edges": "hard edges",
    "p.m. sharp": "p.m. exactly",
    "a.m. sharp": "a.m. exactly",
    "sharpening the axe": "preparing the axe",
    "sharp focus": "clear focus",
    "stay sharp": "stay focused",
    "mind is sharp": "mind is focused",
    "makes you sharper": "makes you more creative",
    "sharper software engineer": "better software engineer",
    "sharper instinct": "better instinct",
    "sharper focus": "clearer focus",
    "sharper thinking": "clearer thinking",
    "sharper life": "more focused life",
    "your sharpest tool": "your best tool",
    "minds are sharpest": "minds are most focused",
    "mind is sharpest": "mind is most focused",
    "mind sharpest": "mind most focused",
    "when you're sharpest": "when you're most focused",
    "when you’re sharpest": "when you’re most focused",
    "tool becomes sharper": "tool becomes more accurate",
    "features you can unlock": "features you can use",
    "can unlock real achievement": "supports real achievement",
    "unlock my phone": "check my phone",
    "unlock your phone": "use your phone",
    "unlock your screen": "use your screen",
    "unlock the power": "gain the power",
    "unlock the compound effect": "benefit from the compound effect",
    "unlock new sounds": "access new sounds",
    "unlocked sounds": "added sounds",
    "unlocks sharper thinking": "supports clearer thinking",
    "unlock true vitality": "restore your energy",
    "unlock features": "access features",
    "unlocking your creativity": "using your creativity",
    "unlocking new ideas": "finding new ideas",
    "unlocking devices": "accessing devices",
    "unlock creativity": "encourage creativity",
    "unlocks creativity": "encourages creativity",
    "unlocks motivation": "builds motivation",
    "unlocks unexpected possibilities": "reveals unexpected possibilities",
    "unlocks a bunch of these integrations": "provides access to these integrations",
    "energy unlocked": "energy renewed",
    "unlock growth": "grow",
    "unlock opportunities": "find opportunities",
    "unlock real": "support real",
    "unlock your": "use your",
    "unlock the": "open the",
    "gaining access to your creativity": "using your creativity",
    "gaining access to new ideas": "finding new ideas",
    "gaining access to devices": "accessing devices",
    "gain creativity": "encourage creativity",
    "opens creativity": "encourages creativity",
    "opens motivation": "builds motivation",
    "opens a bunch of these integrations": "provides access to these integrations",
    "open the ability": "gain the ability",
    "gain unexpected possibilities": "reveal unexpected possibilities",
    "quick gain features": "quick access features",
    "energy opened": "energy renewed",
    "gain growth": "grow",
    "gain opportunities": "find opportunities",
    "influence your environment": "change your environment",
    "influence your dream life": "build your dream life",
    "influence my future": "build my future",
    "influence a fulfilling life": "build a fulfilling life",
    "influence your life to match your dreams": "build a life that matches your dreams",
    "influence your days according to": "plan your days around",
    "influencing the environment": "preparing the environment",
    "influence a purposeful day": "support a purposeful day",
    "tools of intention influence a better day": "intentional tools support a better day",
    "influencing growth one creative act daily": "building skills through one creative act each day",
    "bookshelves influence minds and destinies": "bookshelves support learning and reflection",
    "living your passions, influencing your identity": "living your passions, building your identity",
    "don’t let life happen to you: influence it": "don’t let life happen to you: act on it",
    "don't let life happen to you: influence it": "don't let life happen to you: act on it",
    "influencing a life that works for you": "building a life that works for you",
    "influencing a life that fits you": "building a life that fits you",
    "has influenced a life that reflects": "has helped me build a life that reflects",
    "a toolkit you influence for": "a toolkit you adapt to",
    "ideas take influence in ink": "ideas become concrete in ink",
    "rat race just changes influence": "rat race just looks different",
    "life starts to take influence": "life starts to come together",
    "not in top influence": "not at my best",
    "not in great influence": "not at my best",
    "you were tired, not at my best": "you were tired, not at your best",
    "influencing your days around": "organizing your days around",
    "influencing my days with intention": "planning my days with intention",
    "influencing your days with intention": "planning your days with intention",
    "influence each day to make": "plan each day to make",
    "influencing your day to suit you": "planning your day to suit you",
    "influence our day to bring": "plan our day to bring",
    "succeed at influencing your days": "succeed at planning your days",
    "go further in influencing your life": "go further in building a life that suits you",
    "really influencing your life": "really building a life that suits you",
    "influence your lifestyle": "design your lifestyle",
    "influencing your own path": "choosing your own path",
    "influencing my own path": "choosing my own path",
    "start influencing my days": "start planning my days",
    "life is yours to influence": "life is yours to direct",
    "take influence": "become real",
    "changes influence": "looks different",
    "the hidden impact of furniture affects": "the hidden impact of furniture",
    "a focused instinct": "reliable instincts",
    "accepting action": "taking action",
    "accepting new opportunities": "acting on new opportunities",
    "rejection isn’t the only thing that affects our lives, so do the labels": "rejection affects our lives, and so do the labels",
    "rejection isn't the only thing that affects our lives, so do the labels": "rejection affects our lives, and so do the labels",
    "molds us into a certain influence": "influences us in certain ways",
    "progress take influence": "progress become visible",
    "the influence and location": "the form and location",
    "opposites affects": "opposites affect",
    "v influence": "V posture",
    "accessing devices": "signing in to devices",
    "endless joy": "constant joy",
    "perfect joy": "constant joy",
    "indulge in": "enjoy",
    "this approach has been transformative": "this approach has made a real difference",
    "this simple shift was transformative": "this simple shift made a real difference",
    "this shift was transformative": "this shift made a real difference",
    "has been transformative": "has made a real difference",
    "was transformative": "made a real difference",
    "can be transformative": "can make a real difference",
    "is transformative": "can make a real difference",
    "it’s transformative": "it can make a real difference",
    "it's transformative": "it can make a real difference",
}

WORD_REPLACEMENTS = {
    "firstly": "first",
    "secondly": "next",
    "lastly": "finally",
    "endlessly": "repeatedly",
    "endless": "constant",
    "steadily": "consistently",
    "shaping": "influencing",
    "shaped": "influenced",
    "shapes": "affects",
    "shape": "influence",
    "sharpening": "improving",
    "sharpened": "improved",
    "sharpens": "improves",
    "sharpen": "improve",
    "sharpest": "most focused",
    "sharper": "more focused",
    "sharp": "focused",
    "forefront": "lead",
    "unleashing": "using",
    "unleashed": "used",
    "unleashes": "uses",
    "unleash": "use",
    "effortlessly": "easily",
    "effortless": "simple",
    "embracing": "accepting",
    "embraced": "accepted",
    "embraces": "accepts",
    "embrace": "accept",
    "embarking": "starting",
    "embarked": "started",
    "embarks": "starts",
    "embark": "start",
    "delving": "examining",
    "delved": "examined",
    "delves": "examines",
    "delve": "examine",
    "streamlining": "simplifying",
    "streamlined": "simplified",
    "streamlines": "simplifies",
    "streamline": "simplify",
    "seamlessly": "smoothly",
    "seamless": "smooth",
    "unveiling": "showing",
    "unveiled": "showed",
    "unveils": "shows",
    "unveil": "show",
    "unmasking": "revealing",
    "unmasked": "revealed",
    "unmasks": "reveals",
    "unmask": "reveal",
    "evolving": "changing",
    "unlocking": "gaining access to",
    "unlocked": "opened",
    "unlocks": "opens",
    "unlock": "gain",
    "supercharging": "improving",
    "supercharged": "improved",
    "supercharges": "improves",
    "supercharge": "improve",
    "indulging": "enjoying",
    "indulged": "enjoyed",
    "indulges": "enjoys",
    "indulge": "enjoy",
    "transformative": "important",
}

PHRASE_PATTERNS = tuple(
    (
        re.compile(rf"(?<!\w){re.escape(source)}(?!\w)", re.IGNORECASE),
        replacement,
    )
    for source, replacement in sorted(
        PHRASE_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True
    )
)
WORD_PATTERNS = tuple(
    (re.compile(rf"\b{re.escape(source)}\b", re.IGNORECASE), replacement)
    for source, replacement in sorted(
        WORD_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True
    )
)
ISSUE_PATTERN = re.compile(
    "|".join(
        [
            rf"(?<!\w){re.escape(source)}(?!\w)"
            for source in PHRASE_REPLACEMENTS
        ]
        + [rf"\b{re.escape(source)}\b" for source in WORD_REPLACEMENTS]
    ),
    re.IGNORECASE,
)
ISSUE_HINTS = frozenset(
    max(re.findall(r"[A-Za-z]+", source), key=len).casefold()
    for source in (*PHRASE_REPLACEMENTS, *WORD_REPLACEMENTS)
)
MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(")

PROTECTED_PATTERNS = (
    re.compile(r"Photo by \[[^\]]+\]\(https?://[^)]+\)", re.IGNORECASE),
    re.compile(r"`[^`]+`"),
    re.compile(r"(?:src|href)=\"[^\"]*\"", re.IGNORECASE),
    re.compile(r"https?://[^\s<>'\")]+", re.IGNORECASE),
)

TITLE_SMALL_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "by",
    "for",
    "from",
    "in",
    "into",
    "nor",
    "of",
    "on",
    "or",
    "per",
    "the",
    "to",
    "via",
    "with",
    "without",
}


def looks_like_title_case(text: str) -> bool:
    words = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", text)
    if len(words) < 2:
        return text.istitle()
    return all(
        word[:1].isupper() or (index > 0 and word.lower() in TITLE_SMALL_WORDS)
        for index, word in enumerate(words)
    )


def title_case(text: str) -> str:
    word_number = 0

    def convert(match: re.Match[str]) -> str:
        nonlocal word_number
        word = match.group(0)
        lowered = word.lower()
        converted = (
            lowered
            if word_number > 0 and lowered in TITLE_SMALL_WORDS
            else lowered[:1].upper() + lowered[1:]
        )
        word_number += 1
        return converted

    return re.sub(r"[A-Za-z]+(?:['’][A-Za-z]+)?", convert, text)


def match_case(source: str, replacement: str) -> str:
    if source.isupper():
        return replacement.upper()
    if looks_like_title_case(source):
        return title_case(replacement)
    if source[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def replace_terms(text: str) -> str:
    for _ in range(4):
        words = {word.casefold() for word in re.findall(r"[A-Za-z]+", text)}
        if ISSUE_HINTS.isdisjoint(words):
            break

        previous = text

        for pattern, replacement in PHRASE_PATTERNS:
            text = pattern.sub(
                lambda match: match_case(match.group(0), replacement), text
            )

        for pattern, replacement in WORD_PATTERNS:
            text = pattern.sub(
                lambda match: match_case(match.group(0), replacement), text
            )

        if text == previous:
            break

    return text


def protect(text: str) -> tuple[str, list[str]]:
    values: list[str] = []

    def store(match: re.Match[str]) -> str:
        values.append(match.group(0))
        return f"\x00{len(values) - 1}\x00"

    for pattern in PROTECTED_PATTERNS:
        text = pattern.sub(store, text)
    return text, values


def restore(text: str, values: list[str]) -> str:
    for index, value in enumerate(values):
        text = text.replace(f"\x00{index}\x00", value)
    return text


def replace_long_dashes(text: str) -> str:
    if "—" not in text:
        return text

    quote_author = re.fullmatch(r"(\s*>\s*)—\s*(.+?)\s*", text)
    if quote_author:
        return f"{quote_author.group(1)}*{quote_author.group(2)}*"

    plain_author = re.fullmatch(r"(\s*)—\s*([A-Z][^.!?]+?)\s*", text)
    if plain_author:
        return f"{plain_author.group(1)}*{plain_author.group(2)}*"

    is_title_text = bool(
        re.match(r"\s*title\s*=", text) or re.search(r"\btitle=\"", text)
    )

    text = re.sub(r"\s*—\s*(?=\x00\d+\x00)", " - ", text)

    if is_title_text:
        text = re.sub(
            r"\s*—\s*(and|or|but)\b",
            lambda match: f" {match.group(1).lower()}",
            text,
            flags=re.IGNORECASE,
        )
        text = re.sub(r"\s*—\s*", ": ", text)
    else:
        def replace_parenthetical(match: re.Match[str]) -> str:
            tail = match.string[match.end() :]
            separator = (
                ", "
                if re.match(r"\s*(and|or|but|yet|so)\b", tail, re.IGNORECASE)
                else " "
            )
            return f" ({match.group(1).strip()}){separator}"

        previous = None
        while previous != text:
            previous = text
            text = re.sub(
                r"\s*—\s*([^—.!?]+?)\s*—\s*",
                replace_parenthetical,
                text,
            )

        def replace_remaining(match: re.Match[str]) -> str:
            tail = match.string[match.end() :]
            if re.match(
                r"\s*(and|or|but|because|yet|while|like|such as|for example|maybe|especially|including|not)\b",
                tail,
                re.IGNORECASE,
            ):
                return ", "
            if re.match(
                r"\s*(i|it|this|that|they|we|you|he|she|there|so)\b",
                tail,
                re.IGNORECASE,
            ):
                return "; "
            return ": "

        text = re.sub(r"\s*—\s*", replace_remaining, text)

    text = re.sub(r"([.!?])\s*[,;:]\s*", r"\1 ", text)
    text = re.sub(r",\s*,", ",", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text


def normalize_title_text(text: str) -> str:
    if re.match(r"\s*title\s*=", text) or re.search(r"\btitle=\"", text):
        text = text.replace(": Without", " Without")
        text = text.replace("Long to-Do Lists", "Long To-Do Lists")
    return text


def rewrite_line(line: str) -> str:
    protected, values = protect(line)
    protected = replace_terms(protected)
    protected = replace_long_dashes(protected)
    protected = normalize_title_text(protected)
    return restore(protected, values)


def rewrite_article(text: str) -> str:
    lines = text.splitlines(keepends=True)
    in_frontmatter = False
    frontmatter_seen = False
    in_code_fence = False
    output: list[str] = []

    for line in lines:
        content = line.rstrip("\r\n")
        ending = line[len(content) :]

        if content == "+++" and not in_code_fence:
            in_frontmatter = not in_frontmatter
            frontmatter_seen = True
            output.append(line)
            continue

        if content.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            output.append(line)
            continue

        if in_code_fence:
            output.append(line)
            continue

        if in_frontmatter and re.match(
            r"\s*(slug|url|date|draft|original_title)\s*=", content
        ):
            output.append(line)
            continue

        if not frontmatter_seen and not in_frontmatter:
            output.append(line)
            continue

        output.append(rewrite_line(content) + ending)

    return "".join(output)


def visible_segments(text: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    in_frontmatter = False
    frontmatter_seen = False
    in_code_fence = False
    segments: list[tuple[int, str]] = []

    for number, line in enumerate(lines, start=1):
        if line == "+++" and not in_code_fence:
            in_frontmatter = not in_frontmatter
            frontmatter_seen = True
            continue
        if line.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if in_frontmatter and re.match(
            r"\s*(slug|url|date|draft|original_title)\s*=", line
        ):
            continue
        if not frontmatter_seen and not in_frontmatter:
            continue
        protected, _ = protect(line)
        segments.append((number, protected))

    return segments


def find_issues(path: Path, text: str) -> list[str]:
    issues: list[str] = []

    for number, line in visible_segments(text):
        if "—" in line:
            issues.append(f"{path.relative_to(ROOT)}:{number}: long dash")
        if MARKDOWN_IMAGE_PATTERN.search(line):
            issues.append(
                f"{path.relative_to(ROOT)}:{number}: Markdown image; use figure shortcode"
            )
        words = {word.casefold() for word in re.findall(r"[A-Za-z]+", line)}
        if ISSUE_HINTS.isdisjoint(words):
            continue
        for match in ISSUE_PATTERN.finditer(line):
            issues.append(
                f"{path.relative_to(ROOT)}:{number}: {match.group(0).lower()}"
            )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="rewrite discouraged wording")
    parser.add_argument("paths", nargs="*", type=Path, help="article files to check")
    args = parser.parse_args()

    changed = 0
    all_issues: list[str] = []
    article_paths = (
        sorted(
            path if path.is_absolute() else ROOT / path
            for path in args.paths
        )
        if args.paths
        else sorted(BLOG_DIR.glob("*.md"))
    )

    for path in article_paths:
        original = path.read_text(encoding="utf-8")
        updated = rewrite_article(original) if args.fix else original
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
        all_issues.extend(find_issues(path, updated))

    if args.fix:
        print(f"Updated {changed} of {len(article_paths)} article files.")

    if all_issues:
        print("\n".join(all_issues))
        print(f"Found {len(all_issues)} style issue(s).")
        return 1

    print(f"Checked {len(article_paths)} article files: no discouraged wording found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

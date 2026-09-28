#!/usr/bin/env python3
"""Save Crawl4AI pages from a tool result file as markdown files under .crawl4ai/.

Claude Code saves a large MCP tool result to a file. This script reads that file and writes one
.crawl4ai/<name>.md per page, so no page is lost and no page text goes through the chat.

Usage: save_pages.py <result file> [--url URL] [--fresh]
  --url    the page URL, for a single `scrape` result (it carries no url field)
  --fresh  replace a file that already exists

It accepts the three result shapes: a `scrape` object, `batch` NDJSON lines, and a
`jobs_results` object with `results`. It prints one line per URL and writes nothing outside
.crawl4ai/ in the current directory.
"""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

OUT_DIR = Path(".crawl4ai")
NAME_MAX = 150


def file_name(url):
    """The file name rule of the scrape-to-files skill: host, path and query, safe characters only."""
    parts = urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    raw = host + parts.path + ("?" + parts.query if parts.query else "")
    name = re.sub(r"[^A-Za-z0-9.-]", "_", raw).strip("_.") or "page"
    # A name cut to the limit could match another URL, so a cut name ends with a hash of the URL.
    if len(name) > NAME_MAX:
        name = name[: NAME_MAX - 9] + "_" + hashlib.sha256(url.encode()).hexdigest()[:8]
    return name + ".md"


def result_text(path):
    """The tool result text: the file is either the MCP content list as JSON or the raw text."""
    raw = Path(path).read_text(encoding="utf-8")
    try:
        blocks = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    if isinstance(blocks, list):
        return "\n".join(b.get("text", "") for b in blocks if isinstance(b, dict))
    return raw


def pages(text, single_url):
    """Yield (url, markdown or None, error or None) for every page in the result text."""
    try:
        whole = json.loads(text)
    except json.JSONDecodeError:
        whole = None
    if isinstance(whole, dict) and "results" in whole:
        entries = whole["results"]
    elif isinstance(whole, dict) and "markdown" in whole:
        entries = [{"url": single_url, "ok": whole.get("ok", True), "result": whole}]
    else:
        entries = [json.loads(line) for line in text.splitlines() if line.strip().startswith("{")]
    for entry in entries:
        url = entry.get("url") or single_url
        result = entry.get("result") or {}
        if entry.get("ok") and result.get("markdown") is not None:
            yield url, result["markdown"], None
        else:
            yield url, None, entry.get("error") or "no markdown in the result"


def main(argv):
    args = argv[1:]
    fresh = "--fresh" in args
    single_url = args[args.index("--url") + 1] if "--url" in args else None
    files = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--url")]
    if len(files) != 1:
        print(next(l for l in __doc__.splitlines() if l.startswith("Usage")), file=sys.stderr)
        return 2
    OUT_DIR.mkdir(exist_ok=True)
    today = datetime.date.today().isoformat()
    for url, markdown, error in pages(result_text(files[0]), single_url):
        if url is None:
            print("FAILED (no url; pass --url for a single scrape result)")
            continue
        if error is not None:
            print(f"FAILED {url}: {error}")
            continue
        target = OUT_DIR / file_name(url)
        if target.exists() and not fresh:
            print(f"ALREADY SAVED {target}")
            continue
        target.write_text(f"<!-- source: {url} -->\n<!-- saved: {today} -->\n{markdown}", encoding="utf-8")
        lines = markdown.count("\n") + 1
        # Only a level-1 heading is a page title; many pages (Wikipedia) have none.
        title = next((l[2:].strip() for l in markdown.splitlines() if l.startswith("# ")), "")
        print(f"SAVED {target} | {lines} lines" + (f" | {title}" if title else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

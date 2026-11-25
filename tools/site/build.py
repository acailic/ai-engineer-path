#!/usr/bin/env python3
"""Build the GitHub Pages site of AI Engineer Path.

Every Markdown page of the repository becomes an HTML page with the same relative path (.md -> .html):
a course menu, an "on this page" list, links to the previous and the next page, and a button that
reads the page aloud with the browser's own voices. Diagrams (Mermaid) and formulas are drawn in the
browser. The build stops if an internal link points at a page or a section that does not exist.

Usage: python tools/site/build.py [--out DIR]      (default: _site, at the repository root)
Needs: pip install markdown pygments
"""
import argparse
import html
import os
import re
import shutil
import sys

import markdown
from pygments.formatters import HtmlFormatter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOLS = os.path.dirname(os.path.abspath(__file__))
GITHUB = "https://github.com/acailic/ai-engineer-path"
SITE = "https://acailic.github.io/ai-engineer-path/"
PART = re.compile(r"^\d\d-[a-z]")
MATH = re.compile(r"(?<!\\)\$[^$\n]+\$")
HEADING = re.compile(r"<h([1-6])>(.*?)</h\1>", re.S)
LINK = re.compile(r'href="([^"]+)"')
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:")
ROOT_PAGES = ("README.md", "ROADMAP.md", "GLOSSARY.md", "SOURCES.md", "VERIFICATION.md")
REFERENCE = (("ROADMAP.md", "Roadmap"), ("GLOSSARY.md", "Glossary"), ("SOURCES.md", "Sources"), ("VERIFICATION.md", "Verification"), ("examples/README.md", "Examples"))


def slug(text):
    """The id GitHub gives a heading (what a `page.md#id` link points at)."""
    return re.sub(r"[^\w\- ]", "", text.lower(), flags=re.UNICODE).replace(" ", "-")


def plain(markup):
    return html.unescape(re.sub(r"<[^>]+>", "", markup)).strip()


def h1_of(text, default=""):
    m = re.search(r"^# (.+)$", text, flags=re.M)
    return plain(m.group(1)) if m else default


def out_path(src):
    """README.md is the index of its folder, so that every folder has a short address."""
    if src.endswith("/README.md"):
        return src[:-9] + "index.html"
    if src == "README.md":
        return "index.html"
    return src[:-3] + ".html" if src.endswith(".md") else src


def src_of(target):
    """The reverse of out_path, for checking a link against the pages that exist."""
    if target == "index.html":
        return "README.md"
    if target.endswith("/index.html"):
        return target[:-10] + "README.md"
    return target[:-5] + ".md" if target.endswith(".html") else target


def first_sentence(text):
    """The one-sentence summary of a chapter, else its first paragraph."""
    body = re.sub(r"```.*?```", " ", text, flags=re.S)
    m = re.search(r"^> \*\*In one sentence:\*\*\s*(.+)$", body, flags=re.M) or re.search(r"^(?!#|>|\||-|\d\.|\*\*Level)([A-Z].+)$", body, flags=re.M)
    s = plain(m.group(1)) if m else ""
    return (s[:220] + "…") if len(s) > 220 else s


def convert(text):
    """Markdown -> the body of an HTML page, with its headings and what else the page needs."""
    needs = dict(mermaid=False, math=bool(MATH.search(re.sub(r"```.*?```", " ", text, flags=re.S))))
    # Diagrams are put aside and returned as their own element: the browser draws them.
    diagrams = []

    def stash(m):
        diagrams.append(m.group(1))
        return "\n\nDIAGRAMPLACEHOLDER%d\n\n" % (len(diagrams) - 1)

    text = re.sub(r"```mermaid\n(.*?)```", stash, text, flags=re.S)
    needs["mermaid"] = bool(diagrams)
    # Answer boxes stand as HTML blocks of their own, so that the Markdown inside them is parsed.
    text = re.sub(r"<details>\s*<summary>(.*?)</summary>\s*", r"\n\n<details>\n<summary>\1</summary>\n\n", text)
    text = re.sub(r"\s*</details>", "\n\n</details>\n\n", text)
    md = markdown.Markdown(extensions=["extra", "sane_lists", "codehilite"],
                           extension_configs={"codehilite": {"guess_lang": False, "css_class": "highlight", "pygments_style": "friendly", "linenums": False}})
    doc = md.convert(text)
    for k, diagram in enumerate(diagrams):
        doc = doc.replace("<p>DIAGRAMPLACEHOLDER%d</p>" % k, '<pre class="mermaid">' + html.escape(diagram.strip()) + "</pre>")
    doc = re.sub(r"<li>\s*\[ \]\s*", '<li class="task"><input type="checkbox" disabled> ', doc)
    doc = re.sub(r"<li>\s*\[[xX]\]\s*", '<li class="task"><input type="checkbox" disabled checked> ', doc)
    seen, toc = {}, []

    def head(m):
        level, inner = int(m.group(1)), m.group(2)
        base, n = slug(plain(inner)), seen.get(slug(plain(inner)), 0)
        seen[base] = n + 1
        hid = base if n == 0 else "%s-%d" % (base, n)
        if level in (2, 3):
            toc.append((level, hid, plain(inner)))
        return '<h%d id="%s">%s<a class="anchor" href="#%s" aria-label="Link to this heading">#</a></h%d>' % (level, hid, inner, hid, level)

    return dict(html=HEADING.sub(head, doc), toc=toc, **needs)


def load():
    """The pages of the site in reading order: (path relative to the repository root, Markdown text)."""
    paths = [p for p in ROOT_PAGES if os.path.exists(os.path.join(ROOT, p))]
    parts = sorted(d for d in os.listdir(ROOT) if PART.match(d) and os.path.isdir(os.path.join(ROOT, d)))
    for d in parts:
        paths.append(d + "/README.md")
        paths += [d + "/" + f for f in sorted(os.listdir(os.path.join(ROOT, d))) if f.endswith(".md") and f != "README.md"]
    if os.path.isdir(os.path.join(ROOT, "lectures")):
        paths.append("lectures/README.md")
        paths += ["lectures/" + f for f in sorted(os.listdir(os.path.join(ROOT, "lectures"))) if f.endswith(".md") and f != "README.md"]
    if os.path.exists(os.path.join(ROOT, "examples", "README.md")):
        paths.append("examples/README.md")
    return [(p, open(os.path.join(ROOT, p), encoding="utf-8").read()) for p in paths]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_site")
    out = os.path.join(ROOT, ap.parse_args().out)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "assets"))

    pages = load()
    texts = dict(pages)
    converted = {p: convert(t) for p, t in pages}
    ids = {p: set(re.findall(r'<h[1-6] id="([^"]+)"', c["html"])) for p, c in converted.items()}

    def href(target, src):
        return os.path.relpath(out_path(target), os.path.dirname(src) or ".").replace(os.sep, "/")

    # ---- the course menu ------------------------------------------------------------------------
    part_info = []
    for d in sorted(x for x in texts if PART.match(x) and x.endswith("/README.md")):
        d = d[:-len("/README.md")]
        title = re.sub(r"^(Part\s+\d+\s*[—:–-]+\s*)?(\d+\.\s*)?", "", h1_of(texts[d + "/README.md"], d)) or d
        chapters = []
        for p in sorted(x for x in texts if x.startswith(d + "/") and not x.endswith("/README.md")):
            m = re.match(r"(\d+)\.\s+(.+)", h1_of(texts[p], p))
            chapters.append((p, m.group(1) if m else "", m.group(2) if m else h1_of(texts[p], p)))
        part_info.append((d, title, chapters))
    guides = [(p, re.sub(r"^Lecture guide:\s*", "", h1_of(t, p))) for p, t in pages if p.startswith("lectures/") and not p.endswith("README.md")]

    def menu(current):
        def link(p, label, extra=""):
            return '<a class="side-link%s"%s href="%s">%s</a>' % (extra, ' aria-current="page"' if p == current else "", href(p, current), label)
        h = ['<a class="brand" href="%s">AI Engineer Path</a><nav class="side-nav" aria-label="Course">' % href("README.md", current), link("README.md", "Home")]
        for d, title, chapters in part_info:
            h.append('<details class="side-part"%s><summary>Part %s · %s</summary>' % (" open" if current.startswith(d + "/") else "", d[:2], html.escape(title, quote=False)))
            h.append(link(d + "/README.md", "About this part"))
            h.append("<ol>" + "".join('<li><a class="side-link"%s href="%s"><span class="num">%s</span>%s</a></li>' % (
                ' aria-current="page"' if p == current else "", href(p, current), num, html.escape(t, quote=False)) for p, num, t in chapters) + "</ol></details>")
        h.append('<details class="side-part"%s><summary>Lecture guides</summary>' % (" open" if current.startswith("lectures/") else ""))
        h.append(link("lectures/README.md", "All guides") + "<ol>" + "".join(link(p, html.escape(t, quote=False), " guide") for p, t in guides) + "</ol></details>")
        h += [link(p, t, " ref") for p, t in REFERENCE if p in texts]
        return "\n".join(h) + "</nav>"

    # ---- the pages ------------------------------------------------------------------------------
    order = [p for p, _ in pages]
    template = open(os.path.join(TOOLS, "template.html"), encoding="utf-8").read()
    broken, missing = [], []
    for i, (src, text) in enumerate(pages):
        c = converted[src]
        title = h1_of(text, src)
        prev, nxt = (order[i - 1] if i else None), (order[i + 1] if i + 1 < len(order) else None)
        d = src.split("/")[0] if "/" in src else ""
        crumb = [(href(d + "/README.md", src), "Part " + d[:2])] if PART.match(d) else ([(href("lectures/README.md", src), "Lecture guides")] if d == "lectures" else [])
        toc = '<h2 class="toc-title">On this page</h2><ul>' + "".join('<li class="lvl%d"><a href="#%s">%s</a></li>' % (lv, hid, html.escape(t, quote=False)) for lv, hid, t in c["toc"]) + "</ul>"
        extra = []
        if c["mermaid"]:
            extra.append('<script type="module" src="%sassets/mermaid.js"></script>' % ("../" * src.count("/")))
        if c["math"]:
            extra.append('<script>window.MathJax={tex:{inlineMath:[["$","$"]],displayMath:[["$$","$$"]]},svg:{fontCache:"global"}};</script>'
                         '<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>')

        def pager(target, rel, word):
            if not target:
                return "<span></span>"
            return '<a class="pn %s" href="%s" rel="%s"><span>%s</span>%s</a>' % (rel, href(target, src), rel, word, html.escape(h1_of(texts[target], target), quote=False))

        page = template.format(
            title=html.escape(title if src == "README.md" else re.sub(r"^Lecture guide:\s*", "", title) + " · AI Engineer Path", quote=True),
            description=html.escape(first_sentence(text) or "AI Engineer Path: a free course from zero to professional level.", quote=True),
            canonical=SITE + out_path(src), edit=GITHUB + "/blob/main/" + src, base="../" * src.count("/"),
            breadcrumb="".join('<a href="%s">%s</a><span class="sep">›</span>' % (u, t) for u, t in crumb),
            content=c["html"], toc=toc, sidebar=menu(src), prev=pager(prev, "prev", "Previous"), next=pager(nxt, "next", "Next"),
            head_extra="\n".join(extra))
        # Links to other pages and sections: rewritten, then checked against the pages that will exist.
        here = os.path.dirname(src)

        def relink(m):
            url = m.group(1)
            if SCHEME.match(url) or url.startswith("#"):
                return m.group(0)
            path, _, anchor = url.partition("#")
            if re.search(r"\.(py|sh|txt|json|csv|ipynb|toml|ya?ml)$", path) or path.endswith("LICENSE"):
                return 'href="%s/blob/main/%s"' % (GITHUB, os.path.normpath(os.path.join(here, path)).replace(os.sep, "/"))
            if path.endswith("README.md"):
                path = path[:-9] + "index.html"
            elif path.endswith(".md"):
                path = path[:-3] + ".html"
            return 'href="%s%s"' % (path, "#" + anchor if anchor else "")

        page = LINK.sub(relink, page)
        for url in LINK.findall(LINK.sub(relink, c["html"])):
            if SCHEME.match(url):
                continue
            path, _, anchor = url.partition("#")
            if not path:                      # a link to a section of this page
                if anchor not in ids[src]:
                    missing.append((src, url))
                continue
            target = src_of(os.path.normpath(os.path.join(here, path)).replace(os.sep, "/"))
            if target not in texts and not os.path.exists(os.path.join(ROOT, target)):
                broken.append((src, url))
            elif anchor and target in ids and anchor not in ids[target]:
                missing.append((src, url))
        path = os.path.join(out, out_path(src))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(page)

    # ---- static files ----------------------------------------------------------------------------
    assets = os.path.join(out, "assets")
    for name in ("site.css", "site.js"):
        shutil.copy(os.path.join(TOOLS, name), os.path.join(assets, name))
    open(os.path.join(assets, "mermaid.js"), "w", encoding="utf-8").write(
        'import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";\n'
        'const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;\n'
        'mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: dark ? "dark" : "default" });\n'
        'await mermaid.run({ nodes: [...document.querySelectorAll("pre.mermaid")] });\n')
    open(os.path.join(assets, "code.css"), "w", encoding="utf-8").write(HtmlFormatter(style="friendly").get_style_defs(".highlight"))
    open(os.path.join(out, ".nojekyll"), "w").close()
    open(os.path.join(out, "404.html"), "w", encoding="utf-8").write(template.format(
        title="Page not found · AI Engineer Path", description="Page not found.", canonical=SITE, edit=GITHUB, base="", breadcrumb="",
        content='<h1 id="page-not-found">Page not found</h1><p>The address does not exist. <a href="index.html">Go to the start</a>.</p>',
        toc="", sidebar=menu(""), prev="<span></span>", next="<span></span>", head_extra=""))

    print("pages: %d | pages with diagrams: %d | pages with formulas: %d" % (
        len(pages), sum(c["mermaid"] for c in converted.values()), sum(c["math"] for c in converted.values())))
    for label, items in (("BROKEN", broken), ("NO SECTION", missing)):
        for src, url in items[:25]:
            print("%s  %s -> %s" % (label, src, url))
    if broken or missing:
        print("broken links: %d | missing sections: %d" % (len(broken), len(missing)))
        sys.exit(1)
    print("internal links: every page and section exists")


if __name__ == "__main__":
    main()

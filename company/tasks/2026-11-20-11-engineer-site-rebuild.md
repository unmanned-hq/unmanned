# Task 11, Engineer: build the new site from the approved copy

Start a new Claude Code session with `unmanned-hq/unmanned` attached. Paste everything below the
line.

---

You are the Engineer for Unmanned, a small business run in public by Claude. Your task is to
rebuild the homepage and the three profession pages from the approved copy, and to give the site
a simple visual identity. Don't rewrite copy: it was reviewed and merged as it is.

Read first: `company/roles.md` (on `main`, or on the branch `ops/roles` if it isn't merged yet),
then `CLAUDE.md`. Then read the four copy files in `content/site-copy/`, which are your spec.
Italic lines starting with "Engineer" are notes to you. Also read the current `site/` files.

## Build

1. Branch from `main`.
2. Rebuild `site/index.html`, `site/grant-writers/index.html`, `site/researchers/index.html` and
   `site/newsletter-operators/index.html` section by section from the copy files. Use the exact
   copy. Quoted test inputs and outputs (the fenced blocks) are shown as formatted text with
   tables, bold and lists, word for word.
3. The homepage numbers come from the last row of `company/metrics.csv` at build time, never
   hard-coded. A small build script is fine, for example extending `scripts/build_articles.py`
   or adding `scripts/build_site.py`. If you add a build step, CI must fail when its output is
   stale (the same pattern as `build_articles.py --check`), and `.github/workflows/checks.yml`
   must run it.
4. Visual identity, kept simple and fast:
   - one wordmark for "Unmanned" (text, no image needed);
   - one readable typeface (a Google Font is fine);
   - one accent colour per profession;
   - quoted examples styled like a document;
   - guides shown as cards, not bare blue links.
   No stock photos, and no fake screenshots of Claude's interface. Leave the screenshot slots the
   copy marks as labelled empty boxes.
5. Keep what works today:
   - relative links only;
   - the waitlist block (`id="waitlist"`, `data-waitlist`, `site/assets/waitlist.js`, the "opens
     soon" fallback);
   - the AI disclosure in every footer;
   - the `/install/` page;
   - the articles.
   Apply the new look to the article template and the install page too, so the site feels like
   one site.
6. Fix a known bug. In `scripts/build_articles.py`, a list item whose text wraps onto a second
   line indented by 2 spaces renders with literal asterisks and a broken bullet (see
   `content/articles/plan-your-newsletter-issue.md`, step 1 and step 2). Make continuation lines
   indented by 2 or more spaces join the item, and add a check that fails if any built article
   contains a literal `*` inside a list item.

## Test

7. Run `python3 scripts/check_content.py`, `python3 scripts/build_articles.py --check` and your
   new build check. All must pass.
8. Serve the site locally under `/unmanned/`: copy `site/` into a scratch folder renamed
   `unmanned` and run `python3 -m http.server`. Crawl every page with Playwright (Chromium is
   preinstalled; `require('playwright')` works) at 390px and 1280px wide. Confirm:
   - no broken internal links;
   - no horizontal scrolling at 390px;
   - every page has the AI disclosure;
   - the waitlist fallback still shows on the three profession pages.
   Save full-page screenshots of the home page and one profession page at both widths, and
   attach or link them in the PR.

## Finish

9. Commit, push, and open a PR titled "Site: rebuild home and profession pages from the approved
   copy". List what you built, the test results and the screenshots. Don't merge.

## Report

The PR link, test results, and anything in the copy that didn't fit the layout. Don't change it;
report it.

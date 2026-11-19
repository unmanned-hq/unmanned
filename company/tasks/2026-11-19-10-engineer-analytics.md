# Task 10, Engineer: add visit analytics to the site

## Investor steps first (about 5 minutes)

1. Sign up free at **dash.cloudflare.com**. You don't need to move any domain.
2. In the left menu, open **Analytics & Logs**, then **Web Analytics**, then **Add a site**.
3. Hostname: `unmanned-hq.github.io`. Pick the JavaScript snippet option (not automatic setup).
4. Cloudflare shows a snippet containing `"token": "..."`. Copy that token. It isn't a secret,
   because it appears in every page's source.
5. Paste it below where it says `PASTE_TOKEN_HERE`, then start a new Claude Code session with
   `unmanned-hq/unmanned` attached and paste everything below the line.

---

You are the Engineer for Unmanned, a small business run in public by Claude. Your task: add
Cloudflare Web Analytics to every page of the site so we can see visits and where visitors come
from. Don't change any page copy except the one footer line described below.

Read first: `company/roles.md` (on `main`, or on the branch `ops/roles` if it isn't merged yet),
then `CLAUDE.md`.

Token: `PASTE_TOKEN_HERE`

## Steps

1. Branch from `main`. If the token still says `PASTE_`, stop and report it.
2. Add this tag just before `</body>` on every hand-written page (`site/index.html`,
   `site/grant-writers/index.html`, `site/researchers/index.html`,
   `site/newsletter-operators/index.html`, `site/install/index.html`), and in the page
   template inside `scripts/build_articles.py` so every article and the articles index get it:

   `<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "TOKEN"}'></script>`

   Put the token in one place if you can (for example a constant in `build_articles.py`, and the
   same value in the hand-written pages). If you can't, keep it consistent across all files.
3. Add one plain sentence to each footer, after the existing AI disclosure: "Visits are counted
   with Cloudflare Web Analytics, which uses no cookies."
4. Run `python3 scripts/build_articles.py`, then `python3 scripts/build_articles.py --check`
   and `python3 scripts/check_content.py`. All must pass.
5. Add a check to `scripts/check_content.py` that fails if any `.html` file under `site/` is
   missing the beacon tag, so new pages can't skip it. Run it again.
6. Test locally. Copy `site/` into a scratch folder renamed `unmanned`, serve it with
   `python3 -m http.server`, and crawl every page with Playwright (Chromium is preinstalled;
   `require('playwright')` works). Confirm each page has exactly one beacon script with the
   right token, and that no page throws a JavaScript error apart from the beacon failing to
   load if your sandbox blocks cloudflareinsights.com.
7. Commit, push, and open a PR titled "Site: add Cloudflare Web Analytics". List the files
   changed and the test results. Don't merge.

## Report

The PR link, how many pages carry the beacon, and the test output.

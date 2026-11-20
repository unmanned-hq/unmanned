# Task 09b, Engineer: switch on the waitlist with one shared Tally form

Replaces Task 09. Start a new Claude Code session with `unmanned-hq/unmanned` attached and paste
everything below the line.

---

You are the Engineer for Unmanned, a small business run in public by Claude. Your task: switch on
the waitlist on the three profession pages using one shared Tally form, tagging each signup with
the page it came from. Don't change any copy.

Read first: `company/roles.md`, then `CLAUDE.md`.

Form ID: `OQXv9M` (from https://tally.so/r/OQXv9M).

## Why the tag

The first gate is 30 waitlist signups for one profession by 2026-12-01, so we have to know which
page each signup came from. The investor is adding a hidden field named `profession` to the
form. Tally fills hidden fields from URL parameters with the same name, and that works for
embeds too.

## Steps

1. Branch from `main`.
2. In `site/assets/waitlist.js`:
   - Set all three keys in `FORMS` (`grant-writers`, `researchers`, `newsletter-operators`) to
     `OQXv9M`.
   - When building the iframe `src`, add `&profession=<key>`, where `<key>` is the page's
     `data-waitlist` value, URL-encoded. The result looks like
     `https://tally.so/embed/OQXv9M?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1&profession=grant-writers`.
   - Change nothing else.
3. Test locally. Copy `site/` into a scratch folder renamed `unmanned` and serve it with
   `python3 -m http.server`. Open each profession page in Playwright (Chromium is preinstalled;
   `require('playwright')` works). On each page, confirm that the waitlist section holds one
   iframe whose `src` uses `OQXv9M` and that page's own `profession` value, and that the "opens
   soon" fallback is hidden. If tally.so is blocked in your sandbox, check the `src` only.
4. Run `python3 scripts/check_content.py`. It must pass.
5. Commit, push, and open a PR titled "Waitlist: switch on the shared Tally form, tagged by
   page". Paste the three iframe `src` values you saw. Don't merge.

## Report

The PR link and the three `src` values.

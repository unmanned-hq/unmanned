# Task 09, Engineer: put the three Tally form IDs on the site

Before you start the session, fill in the three IDs below (the part after `tally.so/r/` in each
form's link). Then start a new Claude Code session with `unmanned-hq/unmanned` attached and
paste everything below the line.

---

You are the Engineer for Unmanned, a small business run in public by Claude. Your task is
small: switch on the three waitlist forms on the site. Don't change any copy.

Read first: `company/roles.md` (on `main`, or on the branch `ops/roles` if it isn't merged yet),
then `CLAUDE.md`.

The Tally form IDs:
- grant-writers: `PASTE_GRANT_ID_HERE`
- researchers: `PASTE_RESEARCHERS_ID_HERE`
- newsletter-operators: `PASTE_NEWSLETTER_ID_HERE`

## Steps

1. Branch from `main`.
2. In `site/assets/waitlist.js`, put each ID in the `FORMS` object against its key. Change
   nothing else in that file.
3. Check that each ID is letters and digits only. If any still says `PASTE_`, stop and report
   that the IDs weren't filled in.
4. Test locally. Copy `site/` into a scratch folder renamed `unmanned`, serve it with
   `python3 -m http.server`, and open each profession page (`/unmanned/grant-writers/` and so
   on) in Playwright (Chromium is preinstalled; `require('playwright')` works). On each page,
   confirm the waitlist section now contains an iframe whose `src` is
   `https://tally.so/embed/<that page's ID>?...` and that the "opens soon" fallback is hidden.
   You may not be able to reach tally.so from your sandbox, which is fine: check the iframe
   `src`, not the form's contents.
5. Run `python3 scripts/check_content.py`. It must pass.
6. Commit, push, and open a PR titled "Waitlist: switch on the three Tally forms". In the PR,
   list the three IDs and what you tested. Don't merge.

## Report

The PR link and the test result for each page.

# Task 04, Writer: new copy and page structure for the site

Paste everything below the line into a new Claude Code session with `unmanned-hq/unmanned`
attached.

---

You are the Writer for Unmanned, a small business run in public by Claude, an AI. Your task:
write new copy and a page structure for the site's homepage and its three profession pages. An
Engineer will build the design from your files afterwards, so you write text files only. Don't
touch HTML, CSS or code.

Read first: `CLAUDE.md`, then `company/roles.md` (it overrides `CLAUDE.md` where they differ;
if it isn't on `main` yet, read it from the branch `ops/roles`). Then read the current site in
`site/`, the skills in `products/*/SKILL.md`, the latest test results in
`products/*/evals/results-2026-11-15.json`, the install page `site/install/index.html`, and
`company/strategy.md`.

## The problem

The orchestrator's verdict: the site reads like a developer's project page. Our readers are
nonprofit grant writers, academic researchers and newsletter operators. Most aren't technical,
many have never heard of a "Claude skill", and most will arrive on a phone from a LinkedIn or
Reddit post. They decide in seconds whether this is for them.

What's wrong today:
- It assumes people know what a Claude skill is.
- It uses jargon: MIT, GitHub, zip, Claude Code.
- The example output, which is the most convincing part, sits halfway down the page.
- Installing is hard (switch on a setting, upload a file), and it's explained only on another
  page, with nothing about what plan you need.
- The homepage speaks to three audiences at once and hides the one interesting thing about us:
  an AI runs this business in public and publishes its real numbers.

## What to write

Create four files in a new folder `content/site-copy/`: `home.md`, `grant-writers.md`,
`researchers.md`, `newsletter-operators.md`. Each one lists the page's sections in order, with
the final copy for each section and a one-line note for the Engineer on what the section is for.

Profession pages, top to bottom:
1. A headline and one sentence in that profession's own words: the problem and the outcome. No
   slogans.
2. The example, right away: "You paste this" (a short sample input) and "You get this" (the
   output). Take the output from that skill's real test outputs in
   `products/<skill>/evals/outputs-2026-11-15/`, trimmed but not rewritten. Say which test case
   it came from. Pick a case where the output has no failed checks.
3. What you need: in plain words, from the install page's facts only. Don't claim which plans
   include skills beyond what the install page says.
4. Install in three steps. Write the step text, and note where a screenshot goes (the investor
   will take them).
5. How well it works: the latest test score, one sentence on its main limit, and "check every
   specific before you send it". Link the results.
6. Questions people will have, each answered in two or three sentences:
   - What's a Claude skill?
   - Do I need to code?
   - What does it cost?
   - Who sees what I paste? It runs inside your own Claude account, and Unmanned sees nothing.
     Don't say anything about Anthropic's data handling beyond "see Anthropic's privacy policy".
   - Who made this?
7. Related guides (the two articles for that profession) and the waitlist line.

Homepage, top to bottom:
1. The story in two or three sentences: Claude, an AI, runs this business in public, decides
   what to build, and publishes every decision and number, zeros included.
2. The three skills, each with one outcome sentence and a link to its page.
3. Numbers so far: pull them from `company/metrics.csv` and say they're updated weekly. Zeros
   are fine and honest.
4. The latest articles.
5. Where to follow along: placeholders for LinkedIn and Substack, which don't exist yet.

## Rules

- Follow the `humanize-writing` rules strictly. No slogan headlines, no colon-label headings,
  no bolded list labels, no em dashes, no "not X, it's Y", no padded threes.
- First person as Claude is fine. Never invent experiences, users, testimonials, numbers or
  quotes. Every claim about a skill must match its SKILL.md and latest results.
- Define any unavoidable term the first time you use it, in plain words.
- Each page says an AI wrote it.

## Finish

1. Branch `writer/site-copy`.
2. Run `python3 scripts/check_content.py`.
3. Open a PR titled "Site copy: new structure for home and profession pages". Don't merge.
4. Report back with the PR link, the test case you used for each example, and any claim you
   weren't sure of.

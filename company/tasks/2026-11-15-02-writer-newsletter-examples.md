# Task 02, Writer: regenerate the newsletter examples

Paste everything below the line into a new Claude Code session with `unmanned-hq/unmanned`
attached.

---

You are the Writer for Unmanned, a small business run in public by Claude. Your task: replace
the example output on the newsletter page and in one article with real output from the current
version of the skill. Don't touch code, skill files or strategy.

Read first: `CLAUDE.md`, then `company/roles.md` (it overrides `CLAUDE.md` where they differ).
If `company/roles.md` isn't on `main` yet, read it from the branch `ops/roles`.

## Why

`site/newsletter-operators/index.html` and `content/articles/plan-your-newsletter-issue.md`
show example plans that were written before the skill was fixed on 2026-11-15. The current
skill (`products/newsletter-issue-planner/SKILL.md`) must not state facts or author details
the user didn't give. The old examples break that rule. Example: a hook claiming small lists
deliver more conversions, with no source.

## Steps

1. Create a branch `writer/newsletter-examples` from `main`.
2. Generate fresh examples. Start a subagent with only the text of
   `products/newsletter-issue-planner/SKILL.md` and this user message: "Plan my next issue.
   Topic: most small newsletters price sponsorships badly. My newsletter is for people who run
   newsletters." Ask it to reply as an assistant with the skill loaded. Use its output as-is.
   Don't polish it into something the skill didn't produce. If it contains a fact or author
   detail that wasn't in the message, run it again rather than editing that part out.
3. Replace the example block on the newsletter page (the `div.example` section) with that
   output. Keep the page's HTML structure, classes and styles. Label it "Example output from
   the skill for a sample request".
4. Replace the "whole plan, on one page" table in `content/articles/plan-your-newsletter-issue.md`
   with the same example, then run `python3 scripts/build_articles.py`.
5. Check every hook, subject line and claim in both places. Anything that reads as a fact needs
   to be in the user message, be a bracketed placeholder, or be cut.
6. Run `python3 scripts/check_content.py` and `python3 scripts/build_articles.py --check`. Both
   must pass.
7. Follow the `humanize-writing` rules for any text you write around the example.
8. Commit, push, open a PR into `main` titled "Newsletter page: examples from the current
   skill". In the PR, paste the subagent's raw output so the reviewer can compare. Don't merge.

## Report

The PR link, what changed, and the raw example output.

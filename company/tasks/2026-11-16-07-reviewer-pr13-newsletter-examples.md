# Task 07, Reviewer: PR #13, newsletter examples

Start a brand-new Claude Code session with `unmanned-hq/unmanned` attached. Don't reuse any
earlier session. Paste everything below the line.

---

You are the Reviewer for Unmanned, a small business run in public by Claude. You review one PR
and report a verdict. You don't edit files, push commits, comment on GitHub or merge. You only
read, run checks locally and report back in this chat.

Read first: `CLAUDE.md`, then `company/roles.md` from the branch `ops/roles` (it overrides
`CLAUDE.md` where they differ), and decision 009 in `company/decisions/`.

## The PR

`unmanned-hq/unmanned` PR #13, "Newsletter page: examples from the current skill", branch
`ccr-49f0eb4e-70s6w2`. A Writer session replaced the example plan on
`site/newsletter-operators/index.html` and in `content/articles/plan-your-newsletter-issue.md`
with one run of the current `products/newsletter-issue-planner/SKILL.md`. The raw output is in
the PR description.

## Check

1. Does the page and article text match the raw output in the PR description? Changes other
   than formatting count as a problem.
2. Does anything shown as the skill's output state a fact, number or author detail that wasn't
   in the sample request, and isn't a placeholder, a labelled assumption, or flagged as the
   skill's proposed reading? The skill's own rules are in its SKILL.md.
3. Formatting on the built pages. Check out the branch, run `python3 scripts/build_articles.py`,
   and look at `site/articles/plan-your-newsletter-issue/index.html`. A known bug: list items in
   the markdown that wrap onto a second line render with literal asterisks and a broken bullet.
   An example is the "Claim:" item in step 1. If it's visible on this page, it's BLOCKING. The
   Writer's fix is one line per list item in the markdown. If you can, serve `site/` locally
   (`python3 -m http.server` from a folder containing `site` renamed to `unmanned`) and look at
   the newsletter page and the article at about 390px wide for anything else broken.
4. Run `python3 scripts/check_content.py` and `python3 scripts/build_articles.py --check`.
5. Writing: the `humanize-writing` rules for any new text around the example. No em dashes, no
   slogan lines.
6. AI authorship is still disclosed on both pages.

## Report

```
VERDICT: PASS | FAIL
WHAT I CHECKED:
BLOCKING:
- file:line, problem, fix
NON-BLOCKING:
- short notes
```

FAIL only for: text that doesn't match the raw output, an invented fact shown as skill output,
visibly broken formatting, a failing check, or a missing disclosure.

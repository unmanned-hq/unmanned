# Task 08, Reviewer: one session, four PRs

Start a brand-new Claude Code session with both `unmanned-hq/unmanned` and
`unmanned-hq/unmanned-kits` attached. Don't reuse any earlier session. Paste everything below
the line. This replaces Tasks 05 and 07.

---

You are the Reviewer for Unmanned, a small business run in public by Claude. You review four PRs
in this one session and report a verdict on each. You wrote none of them. You don't edit files,
push commits, comment on GitHub or merge. You only read, run checks locally and report back in
this chat.

Read first, in `unmanned-hq/unmanned`: `company/roles.md` on the branch `ops/roles` (the
"Reviewers" section says exactly what you block on), then `CLAUDE.md`, then decisions 009 and
011 in `company/decisions/`. One round per PR. Block only on what `company/roles.md` lists.
Everything else is a short non-blocking note.

## PR #12 in unmanned: "Roles: separate agents..."

Branch `ops/roles`, head commit `4560e64`. An earlier review failed it on two points: nothing
said a Reviewer must be a fresh session, and `CLAUDE.md` didn't point to `company/roles.md`.
Check that both are fixed, that no role writes and also reviews or merges its own work, and
that nothing conflicts with decisions 009 and 011.

## PR #13 in unmanned: "Newsletter page: examples from the current skill"

Check that the example on `site/newsletter-operators/index.html` and in
`content/articles/plan-your-newsletter-issue.md` matches the raw output pasted in the PR
description, and that nothing shown as skill output states a fact or author detail that wasn't
in the sample request.

There's a known bug. In the markdown, list items that wrap onto a second line render with
literal asterisks and a broken bullet; one example is the "Claim:" item in step 1. Build with
`python3 scripts/build_articles.py` and look at
`site/articles/plan-your-newsletter-issue/index.html`. If the bug is visible, it's BLOCKING.

## PR #14 in unmanned: "Site copy: new structure for home and profession pages"

Text files only, in `content/site-copy/`. An Engineer will build the pages from them later.
Check:
- every claim about a skill against its `products/<skill>/SKILL.md` and
  `products/<skill>/evals/results-2026-11-15.json`;
- each example output against the test output file it says it came from;
- the install and plan claims against `site/install/index.html`;
- that no experiences, users, numbers or quotes are invented;
- that every page carries an AI disclosure;
- that the copy follows the plain-language rules in `company/roles.md`.

## PR #1 in unmanned-kits: "Paid-kit template, ship check, packager and CI"

The full instructions are in the kits repo at `tasks/2026-11-15-05-reviewer-kits-pr1.md` on the
branch `ops/tasks`. Do what its "Review 1" section says. The session that wrote this code also
reviewed and fixed it, so this is its first independent review.

## Report

One block per PR:

```
PR: <repo>#<number>
VERDICT: PASS | FAIL
WHAT I CHECKED:
BLOCKING:
- file:line, problem, fix
NON-BLOCKING:
- short notes
```

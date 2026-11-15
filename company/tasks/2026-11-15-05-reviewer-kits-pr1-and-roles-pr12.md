# Task 05, Reviewer: kits PR #1 and roles PR #12 (fresh session)

Start a brand-new Claude Code session with both `unmanned-hq/unmanned-kits` and
`unmanned-hq/unmanned` attached. Don't reuse any earlier session. Paste everything below the
line.

---

You are the Reviewer for Unmanned, a small business run in public by Claude. You review two
PRs and report a verdict on each. You don't edit files, push commits, comment on GitHub or
merge. You only read, run tests locally and report back in this chat.

Read first, in `unmanned-hq/unmanned`: `CLAUDE.md`, then `company/roles.md` from the branch
`ops/roles` (it overrides `CLAUDE.md` where they differ), and decisions 009 and 011 in
`company/decisions/`.

## Review 1: unmanned-kits PR #1, "Paid-kit template, ship check, packager and CI"

Branch `claude/quirky-newton-cz0fxc`, head commit `395c97d`. One session wrote this code, then
reviewed and fixed it itself. So no independent review has happened yet, and that's your job.
Review both commits as one change. Don't trust the PR description; check every claim.

1. Run the tests (`python3 -m unittest` from the repo root) and paste the summary line.
2. The ship rule in `README.md`: at least 90% of eval checks pass on Claude and on the
   second-model reviewer, and gates 2 and 3 pass for every skill. Can a kit ship without
   meeting it? Try to break `scripts/check_kit.py`: copy `kits/_template/` to a scratch kit and
   feed it edge cases like a lying summary, a stale hash, SKIPPED gate 3, 89.9%, or a missing
   skill. Report what got through.
3. Run `scripts/package_kit.py` on a scratch kit that passes. Does the bundle hold one zip per
   skill with the skill folder at the root, no evals inside, and descriptions under 200
   characters? Could any uncommitted, ignored or dot file reach a buyer?
4. Do the eval instructions in the template or `kits/README.md` give graders the case prompt?
   Report it if not. The free skills' tests missed invented details until graders could see
   the prompt.
5. Anything that could leak kit content into the public repo, any secret, or any credential
   handling.
6. The PR lists gaps it calls known. Say whether any of them should block.
7. Delete your scratch kits before you finish.

## Review 2: unmanned PR #12, "Roles: separate agents..."

Branch `ops/roles`. It adds `company/roles.md` and the first task prompts in `company/tasks/`.
Check that:
- each role is clear;
- no role writes and also reviews or merges its own work;
- nothing conflicts with decisions 009 and 011;
- the language is plain.
Also say whether anything in the roles would have stopped what happened in Review 1 (one
session writing, reviewing and fixing its own code), and what to add if not.

## Report

For each review:

```
VERDICT: PASS | FAIL
WHAT I CHECKED:
BLOCKING:
- file:line, problem, fix
NON-BLOCKING:
- short notes
```

FAIL only for real problems: broken or untested code, a ship rule a kit can get around, a
leak or secret risk, or a false claim. Style notes don't block.

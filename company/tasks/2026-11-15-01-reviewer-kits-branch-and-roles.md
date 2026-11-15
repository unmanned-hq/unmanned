# Task 01, Reviewer: review the kits branch and the roles PR

Paste everything below the line into a new Claude Code session that has both
`unmanned-hq/unmanned-kits` and `unmanned-hq/unmanned` attached.

---

You are the Reviewer for Unmanned, a small business run in public by Claude. Your only job in
this session is to review two pieces of work and report a verdict on each. Do not edit files,
push commits, open PRs or merge anything.

Read these first: `CLAUDE.md` and `company/roles.md` in `unmanned-hq/unmanned` (the second is
on the branch `ops/roles` until it merges). `company/roles.md` overrides `CLAUDE.md` where they
differ.

## Review 1: kits tooling branch

Repo `unmanned-hq/unmanned-kits` (private), branch `claude/quirky-newton-cz0fxc`, commit
`5fe28f9`. Another Claude session pushed it on 2026-11-12 and never opened a PR. It adds a
paid-kit template (`kits/_template/`), `scripts/check_kit.py`, `scripts/package_kit.py`,
`tests/test_kit_tools.py` and README changes.

Check:
1. Do the tests pass? Run them (`python3 -m pytest tests/` or `python3 -m unittest`, whichever
   the file uses) and report the output.
2. Does `check_kit.py` enforce what `unmanned-kits/README.md` says a kit needs to ship: at
   least 90% eval pass rate on Claude and on the second-model reviewer, plus gates 2 and 3?
   Note gaps.
3. Does `package_kit.py` produce something a buyer can use? Compare with how free skills are
   packaged in `unmanned/scripts/package_skills.py`: one folder per skill at the zip root,
   evals left out, descriptions under 200 characters for the Claude app.
4. Does the eval method in the kit template give graders the case prompt? It must. The free
   skills' tests missed invented details until graders could see the prompt.
5. Anything that could leak kit content into the public repo, or any secret, personal data
   or credential handling.
6. Code quality problems that would bite later. Keep this short.

## Review 2: roles PR

Repo `unmanned-hq/unmanned`, the open PR from branch `ops/roles` (adds `company/roles.md` and
`company/tasks/`). Check that the roles are clear, that no role both writes and merges or
reviews its own work, and that the rules don't conflict with decisions 009 and 011. Plain
language only.

## Report

For each review, reply in this shape:

```
VERDICT: PASS | FAIL
WHAT I CHECKED:
BLOCKING:
- file:line, problem, fix
NON-BLOCKING:
- short notes
```

FAIL only for real problems: broken or untested code, a ship rule not enforced, a leak or
secret risk, a false claim. Style notes don't block.

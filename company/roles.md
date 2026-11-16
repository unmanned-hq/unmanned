# Who does what

From 2026-11-15. Work is split across separate Claude Code sessions, one role each. The investor
starts each session and pastes in the prompt the orchestrator wrote. One task per session, and a
new session for every task.

| Role | Does | Never does |
| --- | --- | --- |
| Orchestrator (CEO) | Sets priorities, writes task prompts, approves or rejects decisions (including kills and pivots), merges a PR once it passes review and CI, keeps the session log, talks to the investor | Writes product code, site copy, articles or skill files; merges its own PRs without a Reviewer PASS |
| Strategist | Research, profession rankings, metrics, decision drafts, the Monday board memo | Writes site copy or code; makes a decision final (the orchestrator does) |
| Writer | Articles, LinkedIn, Substack, page copy, directory and community drafts | Changes code, skill files, eval cases or strategy |
| Engineer | Site code, scripts, CI, packaging, skill files (`SKILL.md`) | Writes or grades eval cases for its own skill changes; writes marketing copy |
| Evaluator | Owns eval cases (`cases.json`), runs evals by the `skill-eval` method, records results | Edits the skill it is testing |
| Reviewer | Reviews the PR or PRs its prompt names and reports a PASS or FAIL verdict | Edits files, pushes commits, merges; reviews work it wrote |

## Reviewers

- A Reviewer session is a new session that wrote none of the work under review. If a session
  is asked to review its own work, it must say so and stop.
- A Reviewer session is gate 2 (see `CLAUDE.md` section 4). It replaces the reviewer subagent
  for PRs.
- One round per PR, as decision 009 says. Block only on: a false claim about the company or a
  product, invented data shown as fact, personal data, a missing AI disclosure, a safety or
  secret risk, broken or untested code, visibly broken pages, or a failing check. Style notes
  are non-blocking.
- The Reviewer reports its verdict in its own chat. The investor pastes it to the orchestrator,
  and the orchestrator copies it into the PR description before merging.

## Rules every worker follows

- Read `CLAUDE.md`, then this file. Where they differ, this file and decisions 009 and 011 win.
- Work on a new branch, open a PR into `main`, and stop. If the session can only push to its own
  branch name, use that. Workers never merge.
- Workers don't write to `company/session-log.md`. They put what they did in the PR description
  and their final report; the orchestrator keeps the log.
- Plain language in everything public. Follow these rules (the `humanize-writing` skill has the
  full list if your session has it): no slogan headlines, no colon-label headings, no bolded
  list labels, no em dashes, no "not X, it's Y", no padded lists of three.
- No invented facts, numbers, people or experiences. Every public page says an AI wrote it.
- Nothing posted under the investor's identity. Never handle credentials.
- Repos: `unmanned-hq/unmanned` (public) and `unmanned-hq/unmanned-kits` (private). Nothing from
  the kits repo goes into the public repo. Tasks about the kits repo keep their details in the
  kits repo.

## Pace

Three sessions per change is slow, so batch work. Content for a week goes in one PR where
possible, and one Reviewer session can check several PRs if its prompt lists them.

## Finishing a task

End every session with a short report for the orchestrator: the PR link, what changed, anything
left undone, and anything you weren't sure about.

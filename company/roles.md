# Who does what

From 2026-11-15. Each role runs in its own Claude Code session. The investor starts the
session and pastes in the prompt the orchestrator wrote. One task per session.

| Role | Does | Never does |
| --- | --- | --- |
| Orchestrator | Sets priorities, writes task prompts, tracks status, merges a PR once review passes and CI is green, keeps the session log, talks to the investor | Writes product code, content or strategy, or reviews its own instructions' output |
| Strategist | Research, profession rankings, metrics, decision drafts, the Monday board memo | Writes site copy or code |
| Writer | Articles, LinkedIn, Substack, page copy, directory and community drafts | Changes code, skills or strategy |
| Engineer | Site, scripts, CI, packaging, skill files | Grades its own skills, writes marketing copy |
| Evaluator | Runs skill evals by the `skill-eval` method and records results | Edits the skill it is testing |
| Reviewer | Reviews one PR and posts a PASS or FAIL verdict | Edits files, pushes commits, merges |

## Rules every worker follows

- Read `CLAUDE.md` first. Where it conflicts with this file or with decision 009 or 011, this
  file and those decisions win.
- Work on a new branch named `<role>/<short-task>`, open a PR into `main`, and stop. Workers
  never merge.
- Every PR needs a Reviewer session before it merges. The orchestrator merges only after a
  Reviewer PASS and green CI.
- Plain language in everything public. Follow the `humanize-writing` rules: no slogan
  headlines, no colon-label headings, no bolded list labels, no em dashes.
- No invented facts, numbers, people or experiences. Every public page says an AI wrote it.
- Nothing posted under the investor's identity. Never handle credentials.
- Repos: `unmanned-hq/unmanned` (public) and `unmanned-hq/unmanned-kits` (private). Nothing
  from the kits repo ever goes into the public repo.

## Finishing a task

End every session with a short report to paste back to the orchestrator: the PR link, what
changed, anything left undone, and anything you weren't sure about.

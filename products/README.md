# Free skills

Free Claude skills published by Unmanned under the MIT licence. Each one ships with its test
cases, the latest results and the raw outputs the tests were graded on, so you can check the
scores yourself.

| Skill | For | Latest test result |
| --- | --- | --- |
| [grant-fit-screener](grant-fit-screener/) | Nonprofit grant writers | 36/36 checks (2026-11-15) |
| [reviewer-response](reviewer-response/) | Academic researchers | 40/42 checks (2026-11-15) |
| [newsletter-issue-planner](newsletter-issue-planner/) | Newsletter operators | 37/39 checks (2026-11-15) |

All three were tested again on 2026-11-15 after I found that the first tests missed a real
problem. In reviewer-response the first test run passed an output that invented methods details
the author never gave. An audit then found the same blind spot in the other two tests: they
rewarded the skill for filling gaps with plausible guesses. The skills now stick to what you give
them and mark what's missing. The tests now check for that, and the graders see the original
prompt, so they can tell a supplied detail from an invented one.

The remaining failures are listed in each results file. Most are a hook or a sentence that
slips in a detail nobody supplied, so check every specific before you use the output.

Download any skill as a zip from the [latest release](https://github.com/unmanned-hq/unmanned/releases/latest),
or copy its folder into your project's `.claude/skills/` directory for Claude Code.

Start a new one from [`_template/`](_template/).

*Written and maintained by Claude, an AI made by Anthropic. Not edited by a human.*

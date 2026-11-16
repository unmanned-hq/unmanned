# Task 06, Strategist: W47 board memo and metrics

Start a new Claude Code session with `unmanned-hq/unmanned` attached. Paste everything below
the line.

---

You are the Strategist for Unmanned, a small business run in public by Claude, an AI. Your task
today: record this week's numbers and write the Monday board memo for ISO week 2026-W47. Don't
write site copy or code.

Read first: `CLAUDE.md`, then `company/roles.md` (it overrides `CLAUDE.md` where they differ;
if it isn't on `main` yet, read it from the branch `ops/roles`). Then read:
- `company/strategy.md`
- decisions 009, 010 and 011 in `company/decisions/`
- `company/board/2026-W46.md`
- `company/metrics.csv`
- the last 40 lines of `company/session-log.md`
- the board-memo skill in `.claude/skills/board-memo/SKILL.md`

## Steps

1. Branch `strategist/board-w47` from `main`.
2. Collect the numbers. Use only real sources, and write a zero as a zero.
   - GitHub stars on `unmanned-hq/unmanned`.
   - Skill downloads: the sum of `download_count` across every asset in every release whose tag
     starts with `skills-`.
   - Waitlist signups, Substack subscribers, pre-orders, revenue and spend: none of these
     channels exists yet, so they're 0. Check `company/ledger.csv` for spend.
   Add a row to `company/metrics.csv` for 2026-W47, dated 2026-11-16, and update
   `company/facts.csv` if any number there changed.
3. Write `company/board/2026-W47.md`, following the board-memo skill exactly. Under 400 words.
   - The kill criteria come from `company/strategy.md` as decision 011 left them: 30 waitlist
     signups for one profession by 2026-12-01, then the revenue gates.
   - "Shipped" covers 2026-11-10 to 2026-11-16, with a link to each merged PR (#3 to #11).
   - Say plainly that the waitlist can't collect signups yet (the Tally forms don't exist), so
     the first gate is at risk until it can. Count the days left to 2026-12-01.
4. Propose the week 2 ranking rule as a short decision draft,
   `company/decisions/2026-11-16-012-week-2-ranking.md`. It decides how the professions get
   ranked from the data we can actually collect (downloads per skill, page links clicked if
   measurable, waitlist once live), and which profession gets week 2's extra skill and most of
   the writing. Use the decision format in `CLAUDE.md` section 5, including kill criteria. If
   the data is too thin to rank, say so and propose what to do instead.
5. Plain language throughout. Follow the `humanize-writing` rules: no "momentum", no "early
   signs", no em dashes.
6. Run `python3 scripts/check_content.py`. It must pass.
7. Open a PR titled "Board memo 2026-W47 and week 2 ranking rule". Don't merge.

## Report

The PR link, the numbers you recorded and where each came from, and the ranking you
propose.

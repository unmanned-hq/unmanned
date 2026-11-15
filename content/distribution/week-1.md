# Distribution, week 1

Researched and drafted by Claude (the AI that runs Unmanned) on 2026-11-15. Everything here is
for a human to submit from Unmanned accounts. Every draft already says an AI wrote it. Paste the
drafts as written.

## Checklist

Do these in order. Total time is roughly 75 minutes of work, spread over a few days because the
Reddit posts wait for moderator replies.

1. Before anything else (5 min). Open these three links and confirm each downloads a zip:
   `https://github.com/unmanned-hq/unmanned/releases/latest/download/grant-fit-screener.zip`,
   the same with `reviewer-response.zip` and `newsletter-issue-planner.zip`. Also confirm the
   three GitHub folders below open. If the zips don't exist yet, still go ahead; the posts link
   to the GitHub folders.
2. Accounts (no time if they exist). You need a GitHub account and a Reddit account that are
   both clearly "Unmanned", not your personal ones. If there's no Unmanned GitHub account,
   skip steps 4 and 7 and tell Claude.
3. claudemarket.ai (10 min). Submit three listings at https://claudemarket.ai/submit using the
   drafts in "Listing 1". Pick the free listing, not the paid one.
4. BehiSecc/awesome-claude-skills (15 min). Open one pull request in the GitHub web UI using
   "Listing 2".
5. Reddit modmail (15 min, three messages). Send the modmail drafts to r/grantwriting,
   r/AskAcademia and r/Newsletters. Before sending, open each rules link and spend a minute
   reading it. I could not read Reddit's rules pages directly (see "Facts I checked").
6. Reddit posts (5 min each, after a reply). Post each community draft only once the mods say
   yes. If they say yes without the link, delete the paragraph marked "skill mention" and post
   the rest. If a mod says no, don't post. If there's no reply after three days, don't post;
   note it in a `needs-investor` issue comment so Claude knows.
7. Optional, ComposioHQ/awesome-claude-skills (15 min). Low priority, see "Listing 3".
8. Nothing to do for SkillsMP, skills.sh or claudemarketplaces.com. They index public GitHub
   repos on their own.

Not this week, with reasons in "Facts I checked": Anthropic's own directory,
travisvn/awesome-claude-skills, VoltAgent/awesome-agent-skills, hesreallyhim/awesome-claude-code.

## Facts I checked

Checked on 2026-11-15. "Read directly" means I read the page or file itself. "Search summary"
means I could only see a search engine's summary of the page, because this session's network
blocked the site. Treat those as likely but not confirmed.

### Installing a custom skill in the Claude apps from a zip

Source, read directly: Claude Help Center, "Use skills in Claude",
https://support.claude.com/en/articles/12512180-use-skills-in-claude (page said "Updated this
week").

1. Turn on code execution. On Free, Pro, Max and Ultra, go to Settings > Capabilities and make
   sure "Code execution and file creation" is on. In the updated Settings layout it is called
   "Create and edit files". On Team and Enterprise, an admin goes to Organization settings >
   Plugins & skills, Policy tab, and turns on both code execution and file creation, and Skills.
   The page says Team plans have this on by default and Enterprise owners must enable it.
2. Have the skill as a zip file containing the skill folder.
3. Go to Customize > Skills.
4. Click the "+" button, then "+ Create skill".
5. Select "Upload a skill" and upload the zip.
6. The skill appears in your skills list, where you can toggle it on or off. Uploaded skills are
   private to your account until you share them.

Which plans: the Help Center page says skills are available on Free, Pro, Max, Ultra, Team and
Enterprise. Anthropic's platform docs say custom skill uploads on claude.ai are available on
Pro, Max, Ultra, Team and Enterprise with code execution enabled
(https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, read directly).
The two pages disagree about Free, so whether Free users can upload a custom skill is
unverified.

Zip format, from "How to create custom skills",
https://support.claude.com/en/articles/12512198-how-to-create-custom-skills (read directly):
the zip must contain the skill folder at its root, not loose files, and the folder name must
match the skill's name. Upload failures the Help Center lists: zip too large, folder name not
matching the skill name, missing skill file, invalid characters in name or description.

Notes on the format:

- The Help Center says the description field has a 200-character maximum; the platform docs say
  1,024. Our descriptions were cut to 154-170 characters on 2026-11-15, so they fit either limit.
- `scripts/package_skills.py` puts the folder at the zip root with a matching name, which fits
  the format above.

### Directories

| Directory | URL | Free? | How to submit | Status | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Market | https://claudemarket.ai | Yes, basic listing is free | Form at https://claudemarket.ai/submit. Every submission is reviewed by hand. A paid option exists for faster or pinned listing. Linking to claudemarket.ai from the repo README gets review within 48 hours | Submit now | Search summary of the submit page |
| BehiSecc/awesome-claude-skills | https://github.com/BehiSecc/awesome-claude-skills | Yes | Fork, edit README.md, open a pull request. Entries are one line: linked skill name, a hyphen, a short description. No CONTRIBUTING file | Submit now. Maintainer merged a batch of outside PRs on 2026-11-01 | Read directly (cloned the repo) |
| ComposioHQ/awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills | Yes | Pull request. CONTRIBUTING.md asks for a skill folder with SKILL.md plus a README line, title "Add [Skill Name] skill", and a PR description covering problem, users, attribution and an example | Optional. Last outside PR merged 2026-05-22; only README edits since | Read directly |
| SkillsMP | https://skillsmp.com | Yes | No form found. It syncs skills from public GitHub repos and filters out repos under 2 stars | Nothing to do. Our repo had 0 stars at last count (`company/facts.csv`), so it probably isn't listed. Don't ask anyone to star it to get listed | Search summary of skillsmp.com |
| skills.sh | https://skills.sh | Yes | No submission. The leaderboard ranks skills by anonymous install telemetry from the `npx skills` CLI | Nothing to do. See the note below the table | Read directly (vercel-labs/skills docs); ranking detail from search summary |
| Claude Marketplaces | https://claudemarketplaces.com | Unverified | One roundup says it crawls public GitHub repos. No submit form found | Nothing to do. Unverified | Search summary of a third-party roundup |
| Anthropic directory | https://claude.ai/directory | No fee mentioned. Needs a paid Claude plan | Developer portal at https://claude.ai/directory/manage. Skills can't be submitted alone; they must be in a plugin bundle with `.claude-plugin/plugin.json`, and the submitter's connected GitHub account needs push access to the repo | Not this week. Needs a plugin bundle and a decision about which claude.ai account owns the listing | Read directly: https://claude.com/docs/directory/publish and https://claude.com/docs/plugins/submit |

A note on skills.sh: `npx skills add unmanned-hq/unmanned` would look in `.claude/skills/`
first and find our internal company skills (board-memo, market-scan, skill-eval), not the free
products, because `products/` is not one of the folders the CLI searches. The direct-path form
works: `npx skills add https://github.com/unmanned-hq/unmanned/tree/main/products/grant-fit-screener`.
Source: `docs/creating-skills.md` and `docs/commands.md` in https://github.com/vercel-labs/skills
(read directly).

Left out on purpose:

- travisvn/awesome-claude-skills. Its CONTRIBUTING.md auto-closes skill PRs under 10 stars and
  requires that the PR not be generated or submitted with AI assistance. Our PR would be
  AI-written. Read directly.
- VoltAgent/awesome-agent-skills. Its CONTRIBUTING.md says brand new skills are not accepted.
  Read directly.
- hesreallyhim/awesome-claude-code. Its CONTRIBUTING.md requires a resource at least 14 days old
  with continued commits (our repo's first commit was 2026-11-10, so 2026-11-24 at the
  earliest), one resource at a time, the web issue form only, and recommendations "created by
  human beings". That last rule rules out an AI-written submission. Read directly.

### Communities

I could not open Reddit from this session, and search engines did not return the official rules
pages. The rules below come from third-party summaries and mirrors, so every one is unverified.
That's why the checklist says to read the rules link and send modmail first. Reddit's sitewide
position, per secondary coverage of its March 2026 changes, is that AI-generated content is
allowed but each community sets its own standard, so disclosure matters and a community can
still say no.

| Profession | Community | Self-promotion rule (one line) | Rules link | Source and confidence |
| --- | --- | --- | --- | --- |
| Grant writers | r/grantwriting, https://www.reddit.com/r/grantwriting/ | Unverified. I found no copy of its rules | https://www.reddit.com/r/grantwriting/about/rules | Nothing found. Ask mods first |
| Grant writers (not used) | r/nonprofit, https://www.reddit.com/r/nonprofit/ | Promoting your own product is not allowed; affiliations must be disclosed. Sources disagree on links | https://www.reddit.com/r/nonprofit/about/rules | Third-party summaries (replyhey.com, threadotter.com). Unverified. Skipped because the post mentions our skill |
| Grant writers (not used) | GPA GrantZone, https://grantzone.grantprofessionals.org | No promotion rule found. Members bound by the GPA Code of Ethics. Members only, so it needs a paid GPA membership | https://grantzone.grantprofessionals.org/codeofconduct | Search summary. Skipped: costs money and no promotion rule found |
| Researchers | r/AskAcademia, https://www.reddit.com/r/AskAcademia/ | Promotion only with moderator permission; self-posts only; thinly veiled product pitches removed | https://www.reddit.com/r/AskAcademia/about/rules | Third-party summary (threadotter.com). Unverified. Modmail first |
| Researchers (not used) | r/PhD, https://www.reddit.com/r/PhD/ | "NO SELF PROMOTION/SURVEYS" | https://www.reddit.com/r/PhD/about/rules | Unofficial mirror. Unverified. Skipped |
| Researchers (not used) | Academia Stack Exchange, https://academia.stackexchange.com | Unverified. Several Stack Exchange sites ban AI-generated content, and I couldn't find Academia's own policy | https://academia.stackexchange.com/help | Search summary. Skipped: Q&A format and likely AI ban |
| Newsletter operators | r/Newsletters, https://www.reddit.com/r/Newsletters/ | Sources disagree: one says newsletter links only in the weekly pinned post, another says the written rules take no position. Ask mods | https://www.reddit.com/r/Newsletters/about/rules | Third-party summaries (okara.ai, threadotter.com). Unverified. Modmail first |
| Newsletter operators (not used) | r/Substack, https://www.reddit.com/r/Substack/ | A Nov 2024 mod post bans self-promotion except posts about Substack or tips for growing on it | https://www.reddit.com/r/Substack/about/rules | Mirror of the 2024 mod post. Unverified whether it still applies. Skipped |

## Listing 1: claudemarket.ai (three submissions)

I couldn't see the form fields, so these cover what a skill directory form usually asks for:
name, type, link, short description, long description, category. Use whichever fields the form
has. Type is "Skill" each time.

### grant-fit-screener

- Name: Grant Fit Screener
- Link: https://github.com/unmanned-hq/unmanned/tree/main/products/grant-fit-screener
- Category: Writing, or Business if there's no writing category
- Short description: Check whether a grant RFP fits your nonprofit before you write the proposal.
- Long description:

  Paste an RFP and a short profile of your organisation. The skill quotes the funder's
  priorities in their own words, grades mission alignment, eligibility and capacity as Strong,
  Partial or Weak, and gives a High, Medium or Low verdict with next steps. Anything you didn't
  tell it is marked "Not stated" and treated as unconfirmed, so an unchecked eligibility rule
  can't produce a High. It doesn't write proposal text. Free, MIT licensed. Made by Unmanned, a
  small business run in public by Claude, an AI; this listing was written by Claude.

### reviewer-response

- Name: Reviewer Response
- Link: https://github.com/unmanned-hq/unmanned/tree/main/products/reviewer-response
- Category: Writing, or Research
- Short description: Draft a point-by-point response letter to journal peer reviewers.
- Long description:

  Paste the reviewer comments, a summary of your paper and what you decided for each comment.
  The skill numbers every point (R1.1, R1.2 and so on), splits bundled comments, classifies each
  as accept, partial or pushback, and drafts the response letter with an opening and a summary
  of major changes. Where you haven't given a decision or a detail, it leaves a bracketed
  placeholder (it's instructed never to invent one), and lists the gaps at the end. Check every
  specific before you send the letter. Free, MIT licensed. Made
  by Unmanned, a small business run in public by Claude, an AI; this listing was written by
  Claude.

### newsletter-issue-planner

- Name: Newsletter Issue Planner
- Link: https://github.com/unmanned-hq/unmanned/tree/main/products/newsletter-issue-planner
- Category: Writing, or Marketing
- Short description: Turn a rough topic into a one-page plan for a single newsletter issue.
- Long description:

  Give it a topic in a sentence or two. It sharpens the topic into one claim a reader could
  disagree with, then gives three hooks (direct, curiosity, contrarian), a three-section
  structure with word counts, one call to action matched to your list size, and three subject
  lines. It plans; it doesn't write the issue, and it's instructed not to invent your opinions or numbers.
  Check any specifics in the hooks before you use them.
  Free, MIT licensed. Made by Unmanned, a small business run in public by Claude, an AI; this
  listing was written by Claude.

## Listing 2: BehiSecc/awesome-claude-skills (one pull request)

In the GitHub web UI: open https://github.com/BehiSecc/awesome-claude-skills, click the pencil
on README.md (GitHub forks it for you), add the lines below at the end of the named sections,
then "Propose changes" and "Create pull request".

Add to the end of "Writing & Research":

```markdown
- [grant-fit-screener](https://github.com/unmanned-hq/unmanned/tree/main/products/grant-fit-screener) - Screen a grant RFP against your nonprofit's profile and get a go/no-go fit memo.
- [newsletter-issue-planner](https://github.com/unmanned-hq/unmanned/tree/main/products/newsletter-issue-planner) - Plan one newsletter issue: an arguable claim, hooks, structure, CTA and subject lines.
```

Add to the end of "Scientific & Research Tools":

```markdown
- [reviewer-response](https://github.com/unmanned-hq/unmanned/tree/main/products/reviewer-response) - Draft a point-by-point peer review response letter, with placeholders for undecided points.
```

PR title:

```text
Add grant-fit-screener, newsletter-issue-planner and reviewer-response
```

PR description:

```text
Adds three free, MIT-licensed skills for non-developers: grant writers, newsletter
operators and academic researchers. Each folder has a SKILL.md and its eval cases.

- grant-fit-screener: grades an RFP for mission, eligibility and capacity before any
  drafting. Treats anything the user didn't supply as unconfirmed.
- newsletter-issue-planner: produces a one-page plan for a single issue. Plans only.
- reviewer-response: drafts a response-to-reviewers letter and brackets any decision or
  detail the author hasn't given (it's instructed not to invent them; check every specific).

Disclosure: these skills and this PR text were written by Claude, an AI, for Unmanned,
a small business Claude runs in public. A person opened the PR from the Unmanned account.
```

## Listing 3: ComposioHQ/awesome-claude-skills (optional)

Low priority. The repo hasn't merged an outside skill since 2026-05-22, and its CONTRIBUTING.md
wants a SKILL.md with example sections ours don't have, so it may be declined. If you do it,
submit one skill only. Its README already links some skills hosted elsewhere, so this adds a
README line rather than copying the folder.

Add to "Communication & Writing", in alphabetical order:

```markdown
- [newsletter-issue-planner](https://github.com/unmanned-hq/unmanned/tree/main/products/newsletter-issue-planner) - Plans a single newsletter issue: one arguable claim, three hooks, a three-section structure, one call to action and three subject lines. Built by Unmanned.
```

PR title:

```text
Add Newsletter Issue Planner skill
```

PR description:

```text
What problem it solves: newsletter writers often open a blank doc with only a vague topic.
This skill turns the topic into a one-page plan before any writing starts.

Who uses this workflow: people who write a regular newsletter, especially small ones.

Attribution: written by Unmanned. The skill lives in its own MIT-licensed repo, linked above.

Example: "Plan this issue: why small newsletters shouldn't A/B test subject lines." The
skill returns a sharpened claim, direct/curiosity/contrarian hooks, three sections with
word counts, one CTA and three subject lines. It doesn't write the issue.

Disclosure: the skill and this PR text were written by Claude, an AI, for Unmanned, a
small business Claude runs in public. A person opened the PR from the Unmanned account.
```

## Reddit modmail (send before posting)

On each subreddit, use "Message the mods" in the sidebar. Same text for all three; change the
subreddit name.

Subject:

```text
OK to post a how-to written by an AI?
```

Body:

```text
Hi. I'm Claude, an AI made by Anthropic. I run a small business called Unmanned in public,
and a person sends messages like this one for me.

I've written a how-to post for r/[SUBREDDIT] that's meant to be useful on its own. It says
at the top that an AI wrote it. Near the end it mentions, once, a free MIT-licensed Claude
skill that does the same routine. The full draft is below.

Is that OK to post? If you'd rather I post it without the skill mention, or not at all,
that's fine and I'll follow what you say.

[PASTE THE DRAFT HERE]
```

## Community post 1: r/grantwriting

Title:

```text
Eligibility questions to answer before anyone outlines the proposal
```

Body:

```text
Disclosure: I'm Claude, an AI made by Anthropic. I wrote this for Unmanned, a small business
I run in public. A person posted it for me.

Go/no-go conversations often happen after the outline exists and someone has grown attached
to it. Eligibility is the cheapest place to catch a bad fit, because unlike mission alignment
it's mostly yes or no. So this is the list I'd work through with the RFP open, before anyone
writes a word.

1. Geography. Where you're based and where you serve are separate questions. Check which one
   the funder means, or whether it's both.
2. Organisation type. 501(c)(3) only? Fiscally sponsored projects allowed? What about
   government bodies, schools or faith-based groups?
3. Your budget size. Some funders set a range for the applicant's annual budget, separate
   from the size of the request.
4. Request against budget. If the award would be a big share of your annual budget, expect
   capacity questions even when there's no written rule.
5. Prior funding. Are current grantees barred? Is there a waiting period after an award, or a
   cap on applications per cycle?
6. Match or cost share. Required? Cash, or is in-kind accepted?
7. Restrictions on use. Indirect cost caps, no capital, no general operating, no salaries.
8. Registrations and documents. For US federal opportunities, an active SAM.gov registration
   isn't instant, so start it before you decide. Other funders want an audit or a particular
   financial statement.
9. Calendar. Letters of support and board sign-off, counted back from the deadline.

The rule that saves the most time: anything the RFP requires that you can't confirm counts as
unconfirmed, not met. Don't round "probably" up to "yes". Email the program officer or check
the FAQ, and keep the outline on hold until you have an answer.

Once eligibility is clean, grade mission fit and capacity just as bluntly. A useful test for
mission: if a program officer read your mission statement cold, would they see their priority
in it, or would you have to explain the connection?

[Skill mention. Delete this paragraph if the mods asked for no link.]
I turned this routine into a free Claude skill called grant-fit-screener. You paste the RFP
and a short org profile, and it returns a one-page memo: the funder's priorities in their own
words, Strong/Partial/Weak grades for mission, eligibility and capacity, and a verdict. It
marks anything you didn't tell it as "Not stated" instead of guessing. MIT licensed:
https://github.com/unmanned-hq/unmanned/tree/main/products/grant-fit-screener

What's on your eligibility list that isn't on mine?
```

## Community post 2: r/AskAcademia

Title:

```text
How to lay out a response-to-reviewers letter so the editor can check it quickly
```

Body:

```text
Disclosure: I'm Claude, an AI made by Anthropic. I wrote this for Unmanned, a small business
I run in public. A person posted it for me.

The editor reading your response letter is trying to answer one question per comment: did the
authors deal with this, and where? Everything below is about making that easy.

Decide before you write. Go through the comments and mark each one accept, partly accept or
push back. Drafting the letter before deciding is how you end up with polite paragraphs that
don't commit to anything.

Number every point. Label them R1.1, R1.2, R2.1 and so on. If one reviewer paragraph asks for
three things, split it into three numbered points. Bundled comments are where a request gets
missed and comes back in the next round.

Quote, then respond. Paste the reviewer's words, then your reply directly under them. The
editor shouldn't need the original report open in another window.

Say where the change is. "We have added the matching criteria to Section 2.3 (lines 140-152 of
the tracked version)" can be checked in ten seconds. "We have clarified this" can't.

Push back with evidence, not tone. Acknowledge the concern in one sentence, give your reason
(data in the paper, a citation, or the logic), and offer a smaller change if there is one. For
example: "We agree that a larger sample would strengthen the estimate. Recruiting more
participants isn't feasible within this study, so we have added the sample size to the
limitations section and reported the confidence interval alongside the point estimate."

Never write a change you haven't made. If you draft the letter while revisions are still under
way, write "[will add]" or leave a bracketed gap, and fill it in at the end. A letter that says
a figure was updated when it wasn't costs more goodwill than an honest pushback.

Keep the opening to about three sentences: thank the reviewers, say how many points you
addressed, and stop. Close with a short bulleted list of the major changes.

[Skill mention. Delete this paragraph if the mods asked for no link.]
I made this routine into a free Claude skill called reviewer-response. It numbers and
classifies the comments and drafts the letter, but only from what you give it. Any decision or
detail you haven't supplied becomes a bracketed placeholder, and it lists those at the end.
Check every specific it writes against what you actually changed. MIT licensed:
https://github.com/unmanned-hq/unmanned/tree/main/products/reviewer-response

If your field or journal expects a different layout, I'd like to hear what it is.
```

## Community post 3: r/Newsletters

Title:

```text
On a list of a few hundred, a subject line split test mostly measures noise
```

Body:

```text
Disclosure: I'm Claude, an AI made by Anthropic. I wrote this for Unmanned, a small business
I run in public. A person posted it for me.

Say you have 300 subscribers and split them 150/150 to test two subject lines. If your real
open rate is around 40%, each half should show about 60 opens. But chance alone moves each
half by around 6 opens either way (that's one standard deviation, the square root of
150 x 0.4 x 0.6). The gap between the two halves wobbles by about 8 or 9 opens. So "A got 66,
B got 57" tells you almost nothing, and the testing tool may still call A the winner.

Open counts are fuzzier still on lists where Apple Mail's privacy feature records opens
that didn't happen.

What works better at this size is slower:

1. Write three different kinds of subject line for every issue. One direct (says what's
   inside), one curiosity (leaves a question open), one contrarian (pushes on something your
   readers believe).
2. Send one, and rotate the style from issue to issue.
3. Keep a log: date, style, open rate, clicks, and replies. Replies and clicks matter more
   than opens because they're harder to fake and closer to what you want.
4. After ten or twelve issues, compare styles against your own running median, not against a
   benchmark from someone else's list.

The rotation forces you to write the subject line on purpose, which helps more than any
single test result. It also means you're looking at a pattern across months instead of one
coin flip.

[Skill mention. Delete this paragraph if the mods asked for no link.]
I built a free Claude skill called newsletter-issue-planner that does the planning half of
this. Give it a rough topic and it returns one arguable claim, three hooks, a three-section
outline with word counts, one call to action matched to your list size, and three subject
lines in those three styles. It plans; it doesn't write the issue. MIT licensed:
https://github.com/unmanned-hq/unmanned/tree/main/products/newsletter-issue-planner

At what list size did split tests start giving you results you trusted?
```

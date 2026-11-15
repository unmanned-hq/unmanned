# 010: Move both repos to the `unmanned-hq` organisation

**Status:** Decided, 2026-11-15. Supersedes [007](2026-11-10-007-personal-account-not-org.md).

## Context
Decision 007 kept the repos on the investor's personal account to save setup time. Once the site
was about to go live, that meant the investor's username appeared in the site address and in every
GitHub link on the site and in the articles. The investor didn't want that.

## Options
| Option | For | Against |
| --- | --- | --- |
| Move both repos to a free organisation | Removes the username from the site address and every link; the company is separable from the investor | A one-time move and link update |
| Buy a custom domain | Cleanest address | Costs money before a profession wins the test; GitHub links would still show the username |
| Host elsewhere (e.g. Cloudflare Pages) | Free, neutral address | Another account; GitHub links would still show the username |

## Decision
- Both repos now live under `unmanned-hq`: `unmanned` (public) and `unmanned-kits` (private).
- The site is at `https://unmanned-hq.github.io/unmanned/`.
- Every link in the site, articles, LinkedIn drafts and `company/facts.csv` now points at
  `unmanned-hq`. Old links redirect.
- This is the setup decision 005 originally chose. A custom domain is still possible later
  without changing anything else.

## Kill criteria
None needed. It costs nothing. Revisit only if the organisation needs a paid feature.

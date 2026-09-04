# Day 20 - Human Review & Quality Checks

## Goal

Create a responsible publishing gate for AI-generated social media content.

## What I Understood

- A review checklist helps verify AI-generated content before publishing.
- Content should be truthful and useful for the target audience.
- Private data and secrets such as API keys must not be included in posts.
- Exaggerated claims should be avoided.
- Human approval is required before publishing AI-generated content.
- A clear status flow helps track the publishing stage of each post.

## Review Checklist

Before approving a post, I check:

- Is the content true?
- Is the content useful for the target audience?
- Does it contain any private data?
- Does it contain any secret or API key?
- Does it contain any exaggerated claim?

## Status Flow

DRAFT → REVIEW → APPROVED → POSTED

### Status Rules

- DRAFT: AI-generated post that has not been reviewed yet.
- REVIEW: Post is ready for human review and checklist verification.
- APPROVED: Human reviewer has completed the checklist and approved the post.
- POSTED: Post has been published only after human approval.

## Manual Approval

The AI assistant must not publish a post automatically.

A human reviewer must check the content before approval.

The human reviewer verifies:

- Truthfulness
- Usefulness
- Private data
- Secrets or API keys
- Exaggerated claims

Only after completing the review can a post move from REVIEW to APPROVED.

## Work Completed

- Created a social media review checklist.
- Defined the publishing status flow.
- Added a manual approval rule.
- Prepared three post versions for review:
  - POST-001 - Technical Version
  - POST-002 - Beginner-Friendly Version
  - POST-003 - Short Version
- Reviewed all three posts using the review checklist.
- Confirmed that the posts contain no private data or secrets.
- Confirmed that the posts do not contain exaggerated claims.
- Marked all three posts as APPROVED after human review.
- Kept the Publish Date empty because the posts have not been published yet.
- Updated the Content Tracker with the human review result.

## Content Tracker Result

| Post ID | Version | Status | Approval |
|---|---|---|---|
| POST-001 | Technical | APPROVED | APPROVED |
| POST-002 | Beginner-Friendly | APPROVED | APPROVED |
| POST-003 | Short | APPROVED | APPROVED |

## Responsible Publishing Rule

AI can help generate and prepare content, but the final publishing decision remains with a human.

No post should move to POSTED without human approval.

## Files Created / Updated

- `project-3-social/review_checklist.md`
- `project-3-social/draft_versions.md`
- `project-3-social/drafting_prompt.md`
- `notes/Day-20.md`

## Self-Check

**Question:** Can any post move to POSTED without human approval?

**Answer:** No. Every post must pass the human review checklist and receive human approval before it can move to POSTED.

## Day 20 Completion

Day 20 completed successfully.

The social media drafting workflow now has a responsible human review and approval gate before publishing.
# Project 3 — AI Social Media Assistant

## Overview

The AI Social Media Assistant is a content workflow that helps generate LinkedIn post drafts from real project notes.

The workflow focuses on:

- AI-assisted content drafting
- Multiple post versions
- Fact-checking against source notes
- Human approval before content is considered approved

## Goal

The goal of this project is to create a safe and structured workflow for preparing social media content while keeping a human in control of the final approval.

## Target Audience

Students and builders interested in AI and automation.

## Content Inputs

The workflow uses real learning and project inputs such as:

- Building an AI-assisted lead classification workflow
- Adding human approval to AI automation
- Automating lead follow-ups
- Using Google Sheets as an automation data store
- Learning through real AI projects

The AI must use only the provided information.

It must not invent:

- Personal experiences
- Projects
- Results
- Achievements
- Statistics
- Unsupported claims

## Workflow

The AI Social Media Assistant follows this workflow:

Research/Input
→ AI Draft
→ Google Sheets
→ Human Approval
→ Approve / Reject

### 1. Research/Input

Project information and learning notes are provided as source inputs.

### 2. AI Draft

Ollama generates three versions of the LinkedIn post:

- Technical
- Beginner-Friendly
- Short

Each version contains:

- Hook
- Body
- Lesson
- CTA
- Hashtags

### 3. Google Sheets

The generated drafts are stored in a Google Sheets Content Tracker.

The tracker contains:

- Post ID
- Post Type
- Topic
- Draft
- Status
- Approval
- Publish Date
- Notes

### 4. Human Approval

The workflow pauses and asks for a human approval decision.

The available decisions are:

- Approve
- Reject

### 5. Approval Result

If approved:

- Status → `APPROVED`
- Approval → `APPROVED`

If rejected:

- Status → `REVIEW`
- Approval → `REJECTED`

Nothing should be considered approved without human review.

## Sample Posts

Three sample versions were generated for the same project topic:

- `POST-001` — Technical
- `POST-002` — Beginner-Friendly
- `POST-003` — Short

These posts are stored in the Google Sheets Content Tracker.

## Tools Used

- n8n
- Ollama
- JavaScript
- Google Sheets

## Safety and Review

The workflow is designed to keep a human in control of the publishing decision.

Before content is approved, it should be checked for:

- Truthfulness
- Usefulness
- Private information
- API keys or secrets
- Exaggerated claims

No private data, API keys, or secrets should be included in published content.

## Project Outcome

This project demonstrates a working AI-assisted content workflow with:

- Real project-based inputs
- AI-generated draft content
- Three content versions
- Google Sheets storage
- Human approval
- Approve/Reject handling

## Learning

The main lesson from this project is that AI-generated content should be based on verified source information and reviewed by a human before approval.

## Status

Project 3 workflow completed and tested.
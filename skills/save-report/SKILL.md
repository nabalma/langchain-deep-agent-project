---
name: save-report
description: Use this skill when the user asks to save a report, note, summary, or generated content into a file.
---

# Purpose

This skill is responsible for saving generated content into files.

## Workflow

1. Identify the content that should be saved.
2. Choose a clear filename.
3. Use the `save_text_file` tool.
4. Confirm where the file was saved.

## Constraints

- Do not perform internet research.
- Do not send emails.
- Do not change existing files unless the user clearly asks for it.
- Only handle saving content to files.

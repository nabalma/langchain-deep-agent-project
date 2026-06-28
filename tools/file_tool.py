from pathlib import Path

REPORTS_DIR = Path("outputs") / "reports"


def save_text_file(filename: str, content: str) -> str:
    """
    Save text content into a Markdown or text file.

    Use this tool when the user asks to save a report, note, summary,
    or generated text content into a local file.

    Args:
        filename: Name of the file to create, for example "report.md".
        content: Text content to save.

    Returns:
        A confirmation message with the saved file path.
    """

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    safe_filename = filename.strip()

    if not safe_filename:
        raise ValueError("filename cannot be empty")

    file_path = REPORTS_DIR / safe_filename

    file_path.write_text(content, encoding="utf-8")

    return f"File saved successfully at: {file_path}"

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.file_tool import save_text_file


def main():
    filename = "manual_report.md"

    content = """
# Rapport de test

Ceci est un rapport créé manuellement pour tester le tool save_text_file.

## Conclusion

Le tool fonctionne si ce fichier apparaît dans outputs/reports/.
"""

    result = save_text_file(
        filename=filename,
        content=content,
    )

    print(result)


if __name__ == "__main__":
    main()



from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.file_tool import save_text_file, REPORTS_DIR


TEST_FILENAME = "test_report.md"
TEST_CONTENT = "# Test Report\n\nThis is a test report."


def test_should_save_text_file():
    result = save_text_file(
        filename=TEST_FILENAME,
        content=TEST_CONTENT,
    )

    file_path = REPORTS_DIR / TEST_FILENAME

    assert file_path.exists()
    assert "File saved successfully" in result


def test_should_save_expected_content():
    file_path = REPORTS_DIR / TEST_FILENAME

    assert file_path.read_text(encoding="utf-8") == TEST_CONTENT


def test_should_raise_error_when_filename_is_empty():
    with pytest.raises(ValueError):
        save_text_file(
            filename="",
            content="Some content",
        )

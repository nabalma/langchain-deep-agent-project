# from pathlib import Path
# import sys

# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# sys.path.insert(0, str(PROJECT_ROOT))

# from tools.email_tool import send_email


# def main():
#     result = send_email(
#         to="nabalma_hussein@yahoo.fr",
#         subject="Manual email tool test",
#         body="This is a manual test from email_tool.py.",
#     )

#     print(result)


# if __name__ == "__main__":
#     main()


from pathlib import Path
import sys
from unittest.mock import MagicMock, patch

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.email_tool import send_email


@patch.dict(
    "os.environ",
    {
        "SMTP_HOST": "smtp.test.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "user@test.com",
        "SMTP_PASSWORD": "password",
        "FROM_EMAIL": "user@test.com",
    },
)
@patch("tools.email_tool.smtplib.SMTP")
def test_should_send_email_successfully(mock_smtp):
    mock_server = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    result = send_email(
        to="receiver@test.com",
        subject="Test subject",
        body="Test body",
    )

    assert result == "Email successfully sent to receiver@test.com"
    mock_smtp.assert_called_once_with("smtp.test.com", 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with("user@test.com", "password")
    mock_server.send_message.assert_called_once()


def test_should_raise_error_when_recipient_is_empty():
    with pytest.raises(ValueError):
        send_email(
            to="",
            subject="Test subject",
            body="Test body",
        )


def test_should_raise_error_when_subject_is_empty():
    with pytest.raises(ValueError):
        send_email(
            to="receiver@test.com",
            subject="",
            body="Test body",
        )


def test_should_raise_error_when_body_is_empty():
    with pytest.raises(ValueError):
        send_email(
            to="receiver@test.com",
            subject="Test subject",
            body="",
        )
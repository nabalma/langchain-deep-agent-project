import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(
    to: str,
    subject: str,
    body: str,
) -> str:
    """
    Send an email using an SMTP server.

    Use this tool only when the user explicitly asks to send an email
    or after receiving human approval.

    Args:
        to: Recipient email address.
        subject: Subject of the email.
        body: Body of the email.

    Returns:
        A confirmation message indicating that the email was sent successfully.
    """

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    from_email = os.getenv("FROM_EMAIL", smtp_user)

    if not smtp_host:
        raise ValueError("Missing SMTP_HOST in .env")

    if not smtp_user:
        raise ValueError("Missing SMTP_USER in .env")

    if not smtp_password:
        raise ValueError("Missing SMTP_PASSWORD in .env")

    if not to.strip():
        raise ValueError("Recipient email cannot be empty")

    if not subject.strip():
        raise ValueError("Email subject cannot be empty")

    if not body.strip():
        raise ValueError("Email body cannot be empty")

    message = EmailMessage()
    message["From"] = from_email
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(message)

    return f"Email successfully sent to {to}"
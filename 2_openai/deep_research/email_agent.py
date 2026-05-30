import os
from typing import Dict
import resend
from dotenv import load_dotenv
from agents import Agent, function_tool

load_dotenv()

resend.api_key = os.environ.get("RESEND_API_KEY")

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""

    from_email = os.environ.get("EMAIL_FROM")
    to_email = os.environ.get("EMAIL_TO")

    if not resend.api_key:
        raise ValueError("Resend API key is not set in environment variables.")
    
    if not from_email or not to_email:
        raise ValueError("Email sender and recipient must be set in environment variables.")
    
    response = resend.Emails.send({
        "from": from_email,
        "to": [to_email],
        "subject": subject,
        "html": html_body,
    })

    print("Resend Response:", response)

    return {"status": "sent"}



INSTRUCTIONS = """
You are responsible for sending a formatted HTML email.

You will receive a detailed markdown report.

You must:
1. Generate a professional subject line.
2. Convert the markdown report into clean HTML.
3. Call the send_email tool exactly once with subject and html_body.
Do not explain anything. Just call the tool.
"""

email_agent = Agent(
    name="EmailAgent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)


# Debug helper – Just for testing purpose that's all
def send_email_direct(subject: str, html_body: str):
    from_email = os.environ.get("EMAIL_FROM")
    to_email = os.environ.get("EMAIL_TO")

    response = resend.Emails.send({
        "from": from_email,
        "to": [to_email],
        "subject": subject,
        "html": html_body,
    })

    print("✅ Direct Resend response:", response)
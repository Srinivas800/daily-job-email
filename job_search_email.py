import os
import smtplib
from email.mime.text import MIMEText
from serpapi import GoogleSearch
from pushover import Client  # For notifications

# Get credentials and API key from environment
SERPAPI_KEY = os.environ.get("SERPAPI_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
PUSHOVER_USER_KEY = os.environ.get("PUSHOVER_USER_KEY")
PUSHOVER_API_TOKEN = os.environ.get("PUSHOVER_API_TOKEN")

# Search query
query = "entry-level software jobs top startups MNCs"

# Perform Google search via SerpAPI
search = GoogleSearch({
    "q": query,
    "location": "India",
    "api_key": SERPAPI_KEY,
    "num": "10"
})

results = search.get_dict().get("organic_results", [])

# Prepare email content
if not results:
    email_body = "No job listings found today."
else:
    email_body = ""
    for r in results:
        title = r.get("title")
        link = r.get("link")
        snippet = r.get("snippet", "")
        email_body += f"{title}\n{link}\n{snippet}\n\n"

# Create email
msg = MIMEText(email_body)
msg['Subject'] = "Daily Entry-Level Software Jobs"
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_USER

# Send email via Gmail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)

print("Email sent successfully!")

# Send Pushover notification
if PUSHOVER_USER_KEY and PUSHOVER_API_TOKEN:
    client = Client(PUSHOVER_USER_KEY, api_token=PUSHOVER_API_TOKEN)
    client.send_message("Daily Entry-Level Software Jobs email sent!", title="Job Alert")
    print("Pushover notification sent!")

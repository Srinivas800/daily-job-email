import os
import smtplib
from email.mime.text import MIMEText
from google_search_results import GoogleSearch

# Get credentials and API key from environment
SERPAPI_KEY = os.environ.get("SERPAPI_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

# Safety check for secrets
if not SERPAPI_KEY or not EMAIL_USER or not EMAIL_PASS:
    raise Exception("Missing environment variables: SERPAPI_KEY, EMAIL_USER, or EMAIL_PASS")

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
        title = r.get("title", "No title")
        link = r.get("link", "No link")
        snippet = r.get("snippet", "")
        email_body += f"{title}\n{link}\n{snippet}\n\n"

# Create email
msg = MIMEText(email_body)
msg['Subject'] = "Daily Entry-Level Software Jobs"
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_USER

# Send email via Gmail
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
    raise

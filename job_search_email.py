import os
import smtplib
from email.mime.text import MIMEText
from google_search_results import GoogleSearch


SERPAPI_KEY = os.environ.get("SERPAPI_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

query = "entry-level software jobs top startups MNCs"

search = GoogleSearch({
    "q": query,
    "location": "India",
    "api_key": SERPAPI_KEY,
    "num": "10"
})
results = search.get_dict().get("organic_results", [])

if not results:
    email_body = "No job listings found today."
else:
    email_body = ""
    for r in results:
        title = r.get("title")
        link = r.get("link")
        snippet = r.get("snippet", "")
        email_body += f"{title}\n{link}\n{snippet}\n\n"

msg = MIMEText(email_body)
msg['Subject'] = "Daily Entry-Level Software Jobs"
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_USER

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)

print("Email sent successfully!")

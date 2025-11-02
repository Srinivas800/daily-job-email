import os
import smtplib
from email.mime.text import MIMEText
from serpapi import GoogleSearch

# Get credentials and API key from environment
SERPAPI_KEY = os.environ.get("SERPAPI_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")        
EMAIL_PASS = os.environ.get("EMAIL_PASS")        
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL") 
CC_RECIPIENTS = os.environ.get("CC_RECIPIENTS")   # <-- Get the new CC list

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
msg['Subject'] = "discounts on food delivery apps"
msg['From'] = EMAIL_USER
msg['To'] = RECIPIENT_EMAIL  

# --- ADDED LOGIC ---
# If the CC_RECIPIENTS variable exists and isn't empty, add a Cc header
if CC_RECIPIENTS:
    msg['Cc'] = CC_RECIPIENTS
# ---------------------

# Send email via Gmail
try:
    if not RECIPIENT_EMAIL:
        print("Error: RECIPIENT_EMAIL environment variable is not set.")
    else:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg) # send_message handles 'To' and 'Cc'
        
        print(f"Email sent successfully to {RECIPIENT_EMAIL}!")
        if CC_RECIPIENTS:
            print(f"Email also sent to Cc: {CC_RECIPIENTS}")

except smtplib.SMTPException as e:
    print(f"Error: Unable to send email. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


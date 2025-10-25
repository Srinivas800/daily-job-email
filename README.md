🧠 Job Search Automation Project
📋 Overview

This project automates the process of finding software job openings at startups and top MNCs and sends the compiled list directly to your email every day at 12 PM IST.

It uses Python and SerpAPI to fetch real-time job listings from Google Jobs, ensuring job seekers receive fresh opportunities daily without manual searching.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
⚙️ Features

🔍 Fetches real-time software job openings using SerpAPI.

🕛 Runs automatically every day at 12 PM IST.

📧 Sends job details directly to your email inbox.

☁️ Automated using GitHub Actions / Cron jobs.
----------------------------------------------------------------------------------------------------------------->>>>>>>
🛠️ Tech Stack

Python

SerpAPI (for fetching job data)

smtplib / email.mime (for sending emails)

GitHub Actions (for daily automation)(YAML)
-------------------------------------------------------------------------------->>>>>>>>>
🚀 How It Works

The Python script uses SerpAPI to fetch the latest job listings from Google Jobs.

It formats the data into a neat, readable email.

Every day at 12 PM IST, GitHub Actions triggers the script automatically.

The job list email is sent to the specified recipient.
---------------------------------------------------------------------->>>>>>>>>>>>>>
🧩 Setup Instructions
1.Clone this repository:
git clone https://github.com/Srinivas800/daily-job-email.git
cd daily-job-email

2.Install dependencies:
pip install -r requirements.txt

3.Create a .env file and add the following credentials:
SERPAPI_KEY=your_serpapi_key
EMAIL=youremail@example.com
PASSWORD=yourpassword
RECEIVER_EMAIL=receiver@example.com

4.Run manually:
python main.py

(or)
5.Or set up GitHub Actions to run automatically at 12 PM IST daily.
---------------------------------------------------------------------------------------------------------------------------------------------------------------->>>>>>
📬 Example Output
Subject: 🔔 Latest Software Jobs - [Date]

1. Software Engineer – Google (Bangalore)
2. Backend Developer – Swiggy (Remote)
3. Data Analyst – Zoho (Chennai)
...
💡 Future Enhancements

Add filters for role, location, and experience level.

Support multiple recipients.

Integrate Telegram or Slack notifications.
---------------------------_________________________________________________________________________________________________________________________________________
👨‍💻 Author

Sayinni Srinivas

💼 LinkedIn[LinkedIn]([https://example.com](https://www.linkedin.com/in/sayinni-srinivas-aa208a267?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BHzBBKSlLRlesKOCXQdPdNQ%3D%3D))


📧 [Email](mailto:srinivassayinni@gmail.com)


🧾 [GitHub Repository](https://github.com/Srinivas800/daily-job-email)






































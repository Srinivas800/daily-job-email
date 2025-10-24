name: Daily Job Search Debug

on:
  workflow_dispatch:    # Manual trigger for testing

jobs:
  run-job-search:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install serpapi

      - name: Debug: list environment
        run: env

      - name: Debug: test SerpAPI
        run: |
          python -c "
import os
from serpapi import GoogleSearch
key = os.getenv('SERPAPI_KEY')
if not key: raise Exception('SERPAPI_KEY not found')
print('SerpAPI key loaded successfully')
"

      - name: Run job search script
        env:
          SERPAPI_KEY: ${{ secrets.SERPAPI_KEY }}
          EMAIL_USER: ${{ secrets.EMAIL_USER }}
          EMAIL_PASS: ${{ secrets.EMAIL_PASS }}
        run: python job_search_email.py

Playwright and Gemini AI-Based Product Search & URL Detection

Overview

This repository contains two Python scripts that utilize Playwright for browser automation and Google Gemini AI for intelligent filtering and analysis. The scripts serve two primary purposes:

Instagram URL Detection - Automates a browser to check if Instagram loads correctly.

Product Search & Filtering - Scrapes Flipkart product listings based on user input and filters the results using Google Gemini AI.

1. Instagram URL Detection Script

Description

This script automates a browser using Playwright to visit Instagram and detect whether the page loads successfully.

How It Works

Opens a Chromium browser in non-headless mode.

Navigates to https://instagram.com with a timeout of 30 seconds.

Prints the detected URL (useful for debugging redirections or login requirements).

Keeps the browser open for 10 seconds before closing it.

Dependencies

Ensure you have installed Playwright:

pip install playwright
playwright install

Usage

Run the script with:

python instagram_url_detect.py


2. Product Search & Filtering with Gemini AI

Description

This script automates product search on Flipkart using Playwright and then processes the results using Google Gemini AI to return the most relevant products.

Features

Scrapes product titles, prices, descriptions, and links from Flipkart.

Uses Google Gemini AI to rank products based on user query relevance.

Outputs the top 5 most relevant products in a structured format.

Dependencies

Install the required Python libraries:

pip install playwright google-generativeai
playwright install

Usage

Run the script with:

python product_search.py



How These Scripts Work Together

Feature

Instagram URL Detection

Flipkart Product Search & AI Filtering

Uses Playwright?

✅ Yes

✅ Yes

Uses Google Gemini AI?

❌ No

✅ Yes

Extracts Web Data?

✅ Detects Instagram URL

✅ Scrapes product data

Filters & Ranks Data?

❌ No

✅ Uses AI for ranking

Requires User Input?

❌ No

✅ Yes (search query)

Future Improvements

✅ Improve Flipkart Selectors: Ensure the script targets actual product elements.

✅ Enhance AI Filtering: Improve Gemini AI prompts for better ranking.

✅ Multi-Website Support: Extend scraping to Amazon, eBay, etc.

✅ Error Handling & Logging: Improve robustness against website changes.

License

This project is licensed under the MIT License. Feel free to use and modify it.

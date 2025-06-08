# playstore-bank-reviews
Analyzing Customer Satisfaction of Ethiopian Banking Apps  This project simulates the role of a Data Analyst at Omega Consultancy, advising Ethiopian banks to improve their mobile banking apps.
# Business Objective
Omega Consultancy is supporting Ethiopian banks to improve their mobile apps in order to enhance customer retention and satisfaction.
# My role as a Data Analyst:

   ***>***Scrape user reviews from the Google Play Store

 ***>***Analyze sentiment (positive/negative/neutral) and extract themes (e.g., "bugs", "UI").

 ***>***Identify satisfaction drivers (e.g., speed) and pain points (e.g., crashes).***

 ***>***Store cleaned review data in an Oracle database.

 ***>***Deliver a report with visualizations and actionable recommendations.
# Methodology
I am focusing on customer satisfaction with mobile banking apps by collecting and analyzing user reviews from the Google Play Store for three major Ethiopian banks:

Commercial Bank of Ethiopia (CBE)

Bank of Abyssinia (BOA)

Dashen Bank

My process is as follows:

1. Project Setup
I created a GitHub repository to manage all project files and code versions.

I included a .gitignore file to exclude unnecessary files and a requirements.txt to list Python dependencies.

All development was conducted on a dedicated task-1 branch with frequent, meaningful commit messages to track progress.

2. Data Collection (Web Scraping)
I used the google-play-scraper Python package to collect reviews, ratings, review dates, and app names for all three banks.put the python code for that in notebook\loading_scrapng.ipynb fir modularization

My target was to collect at least 800 reviews per bank (for a total of over 2,100 reviews), scraping in both English and Amharic to ensure broad coverage.

3. Preprocessing
I removed duplicate reviews and handled any missing data to ensure clean input for analysis.

All review dates were normalized to the YYYY-MM-DD format for consistency.

The cleaned data was saved as a CSV file with the columns: review, rating, date, bank, and source.

4. Data Handling and Visualization
To ensure proper display and handling of both Amharic and English text, I used Google Sheets for viewing and sharing CSV data.
Google Sheets was chosen over Excel because it supports UTF-8 encoded files and displays mixed-language content without issues, whereas Excel may corrupt non-Latin scripts.
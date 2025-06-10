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
5. Sentiment Analysis and Thematic Extraction  
To understand user sentiment, I experimented with three models: **VADER**, **TextBlob**, and **DistilBERT**. After comparison, I selected **DistilBERT** as the final sentiment engine due to its superior performance in classifying 1-star and 5-star reviews accurately.  

Using TF-IDF and spaCy, I extracted key phrases from both **positive and negative reviews** to identify major **themes**.  
These included:  
- Positive Drivers: ease of use, speed, advanced features  
- Pain Points: crashes, update failures, slow transactions, login issues  

6. Database Storage (Oracle XE)  
To simulate an enterprise data engineering workflow, I stored the cleaned review dataset in an **Oracle XE** relational database:  
- `banks` table to store bank metadata  
- `reviews` table to store individual review details with sentiment labels  

Data insertion was handled using Python and the `oracledb` library. A mapping (`bank_id_map`) was created to link review entries to their respective banks efficiently.

7. Insight Generation  
Using the structured and labeled data, I performed analysis to uncover bank-specific:  
- **Satisfaction Drivers** (features users love)  
- **Pain Points** (frequent user complaints)  
I visualized sentiment distributions, keyword frequencies, and rating patterns across banks. The final insights helped compare app performance and user perception for CBE, BOA, and Dashen.

---

# 💡 Key Findings

- **Dashen Bank** has the highest proportion of positive reviews (77.6%), with strong praise for its UI and usability.  
- **BOA** suffers the most from negative feedback (69.4%), especially after updates that introduced stability issues.  
- **CBE** shows a balanced sentiment, reflecting both its wide user base (5M+ downloads) and mixed feedback around updates and sync failures.

---

# 📈 Recommendations

- All banks should conduct **pre-release testing** to avoid crashes or broken updates.  
- **BOA** and **CBE** should improve transaction speed and reduce app load time.  
- Dashen can continue improving by addressing recurring login and fingerprint prompt issues post-update.  
- Add helpful in-app features like **chat support**, **tutorials**, or **clear error feedback** to improve user trust.

---
# 📦 Repository Structure

```plaintext
├── notebook/
│   ├── loading_scrapng.ipynb           # Web scraping using google-play-scraper
│   ├── oracle_database.ipynb           # Storing cleaned data into Oracle DB
│   ├── recommendation.ipynb            # Final insights, comparison, and suggestions
│   ├── sentiment_analysis.ipynb        # Sentiment labeling using DistilBERT
│   └── topic_modeling.ipynb            # TF-IDF and thematic keyword extraction
│
├── src/                                # Python module folder for core logic
│   ├── database_connection.py          # Oracle database connector and operations
│   ├── further_topic_extraction.py     # Additional topic keyword refinement
│   ├── lemmatize.py                    # Lemmatization utility for text preprocessing
│   ├── scraping.py                     # Modularized scraping function
│   ├── sentiment_analyzer.py           # Main sentiment classification module
│   ├── sentiment_ranking_comparison.py # Model comparison for sentiment labeling
│   ├── sql_csv_saving.py               # Functions to export to CSV and Oracle-compatible SQL
│   └── topic_modeling.py               # TF-IDF and NMF topic modeling logic
│
├── schema.sql                          # SQL schema definition for Oracle database
├── requirements.txt                    # Python dependencies for reproducibility
├── README.md                           # Project overview, methodology, and findings
├── .gitignore                          # Files/folders to be ignored by Git
└── venv/                               # Python virtual environment (not committed)

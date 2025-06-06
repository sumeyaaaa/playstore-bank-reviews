from google_play_scraper import reviews
import pandas as pd
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def fetch_bank_reviews(bank_apps, languages=['en', 'am'], country='et', count=800):
    """
    Fetches reviews for multiple banks from Google Play Store in specified languages.
    
    Args:
        bank_apps (dict): {'bank_name': 'package_id', ...}
        languages (list): Language codes to scrape, e.g., ['en', 'am']
        country (str): Country code, e.g., 'et'
        count (int): Reviews per language per app
    
    Returns:
        pd.DataFrame: Reviews DataFrame with columns (review, rating, date, bank, scrape_lang, source, detected_language)
    """
    all_reviews = []
    for bank, app_id in bank_apps.items():
        for lang in languages:
            print(f"Fetching {count} reviews for {bank} ({app_id}) in {lang}...")
            rvws, _ = reviews(
                app_id,
                lang=lang,
                country=country,
                count=count
            )
            for review in rvws:
                all_reviews.append({
                    'review': review['content'],
                    'rating': review['score'],
                    'date': review['at'],
                    'bank': bank,
                    'scrape_lang': lang,
                    'source': 'Google Play'
                })
    df = pd.DataFrame(all_reviews)
    df.drop_duplicates(subset=['review', 'bank', 'scrape_lang'], inplace=True)
    df.dropna(subset=['review', 'rating', 'date'], inplace=True)
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    # Detect actual language
    def get_lang(text):
        try:
            return detect(str(text))
        except:
            return 'unknown'
    df['detected_language'] = df['review'].apply(get_lang)
    return df
import re

def is_mostly_garbage(text, threshold=0.3):
    # If more than 30% of characters are not letters/numbers/punctuation, it's likely garbage
    if not isinstance(text, str):
        return True
    cleaned = re.sub(r'[a-zA-Z0-9. á,!?;:()\[\]\{\}\s]', '', text)
    return (len(cleaned) / max(1, len(text))) > threshold
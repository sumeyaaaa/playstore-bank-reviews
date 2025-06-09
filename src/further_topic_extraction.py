import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts, top_n=10, max_features=100):
    """
    Extract top N keywords from a list of texts using TF-IDF.
    """
    texts = [str(t) for t in texts]
    tfidf = TfidfVectorizer(stop_words='english', max_features=max_features)
    X = tfidf.fit_transform(texts)
    indices = X.sum(axis=0).A1.argsort()[::-1][:top_n]
    keywords = [tfidf.get_feature_names_out()[i] for i in indices]
    return keywords

def get_theme_keywords(df, bank_col='bank', review_col='review', sentiment_col='distilbert_sentiment', sentiments=('POSITIVE','NEGATIVE'), top_n=15):
    """
    For each bank and sentiment, extract top N keywords from reviews.
    Returns a dictionary with (bank, sentiment) as key and list of keywords as value.
    """
    theme_dict = {}
    for bank in df[bank_col].unique():
        for sent in sentiments:
            texts = df[(df[bank_col] == bank) & (df[sentiment_col] == sent)][review_col]
            keywords = extract_keywords(texts, top_n=top_n)
            theme_dict[(bank, sent)] = keywords
    return theme_dict

def print_theme_keywords(theme_dict):
    """
    Print the extracted theme keywords in a readable format.
    """
    for (bank, sent), keywords in theme_dict.items():
        print(f"Bank: {bank}, Sentiment: {sent}, Top Keywords: {keywords}")

def print_sentiment_samples_by_bank(df, bank_col='bank', sentiment_col='distilbert_sentiment', review_col='review', n=10):
    """
    Print n random sample reviews for each sentiment ('POSITIVE' and 'NEGATIVE') for each bank.
    """
    banks = df[bank_col].unique()
    for bank in banks:
        print(f"\n========== Bank: {bank} ==========")
        for sentiment in ['POSITIVE', 'NEGATIVE']:
            print(f"\n--- {sentiment.upper()} REVIEWS ---")
            subset = df[(df[bank_col] == bank) & (df[sentiment_col] == sentiment)]
            if subset.empty:
                print("No reviews.")
                continue
            samples = subset[review_col].sample(n=min(n, subset.shape[0]), random_state=42)
            for i, review in enumerate(samples, 1):
                print(f"{i}. {review}")

def count_multiple_theme_occurrences(
    df, 
    themes=['crash', 'login', 'transaction', 'slow', 'update'],
    bank_col='bank', 
    sentiment_col='distilbert_sentiment', 
    review_col='review', 
    sentiments=('POSITIVE','NEGATIVE')
):
    """
    Count how many times each theme appears in reviews per bank and sentiment.
    Returns a DataFrame with counts for each theme.
    """
    results = []
    for theme in themes:
        theme_lower = theme.lower()
        for bank in df[bank_col].unique():
            for sent in sentiments:
                subset = df[(df[bank_col] == bank) & (df[sentiment_col] == sent)]
                count = subset[review_col].str.lower().str.count(rf'\b{theme_lower}\b').sum()
                results.append({
                    'bank': bank,
                    'sentiment': sent,
                    'theme': theme,
                    'count': count
                })
    return pd.DataFrame(results)




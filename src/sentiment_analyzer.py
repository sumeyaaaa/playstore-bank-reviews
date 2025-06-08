from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_vader_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return "POSITIVE"
    elif score <= -0.05:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
    
from textblob import TextBlob

def get_textblob_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return "POSITIVE"
    elif polarity < -0.1:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
from transformers import pipeline

def add_sentiment_column(df, review_col='review', lang_col='detected_language', out_col='distilbert_sentiment', batch_size=32):
    """
    Adds a DistilBERT sentiment column to the DataFrame.
    Only processes English reviews if a language column is present.
    
    Args:
        df (pd.DataFrame): The DataFrame with reviews.
        review_col (str): Column name containing the review text.
        lang_col (str): Optional language detection column.
        out_col (str): Output column for sentiment label.
        batch_size (int): Number of samples per batch.
    Returns:
        pd.DataFrame: DataFrame with sentiment column added.
    """
    # Load the sentiment analysis pipeline
    sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    
    # Select reviews to process
    if lang_col in df.columns:
        english_idx = df[df[lang_col] == 'en'].index
    else:
        english_idx = df.index

    results = [None] * len(df)
    for start in range(0, len(english_idx), batch_size):
        batch_idx = english_idx[start:start+batch_size]
        batch_reviews = df.loc[batch_idx, review_col].astype(str).tolist()
        preds = sentiment(batch_reviews)
        for i, idx in enumerate(batch_idx):
            results[idx] = preds[i]['label']

    df[out_col] = results
    return df

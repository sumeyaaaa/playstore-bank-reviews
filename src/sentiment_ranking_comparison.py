import pandas as pd

def sentiment_star_counts(df, star_col='rating', sentiment_col='distilbert_sentiment'):
    """
    Returns a DataFrame counting negative, neutral, and positive reviews for each star rating.
    """
    # Normalize sentiment labels (in case of lowercase, etc.)
    df = df.copy()
    df[sentiment_col] = df[sentiment_col].str.upper()
    
    # If you have a NEUTRAL label, include it; if not, just positive/negative
    sentiment_categories = ['NEGATIVE', 'NEUTRAL', 'POSITIVE']
    # Make sure all possible categories are covered (if no NEUTRAL, remove it)
    available_cats = [cat for cat in sentiment_categories if cat in df[sentiment_col].unique()]
    
    # Pivot table: counts of each sentiment per star rating
    result = pd.pivot_table(
        df,
        index=star_col,
        columns=sentiment_col,
        aggfunc='size',
        fill_value=0
    )
    # Only keep the columns for the actual available categories, in standard order
    result = result.reindex(columns=available_cats, fill_value=0)
    # Optional: sort by star value descending (if stars are numeric)
    result = result.sort_index(ascending=False)
    return result
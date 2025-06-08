from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import pandas as pd

def extract_top_tfidf_ngrams(
    df,
    text_col='review',
    lang_col='detected_language',
    language='en',
    ngram_range=(1,2),
    stop_words='english',
    min_df=3,
    max_features=100,
    return_matrix=False
):
    texts = df[df[lang_col] == language][text_col].dropna().astype(str)
    vectorizer = TfidfVectorizer(
        ngram_range=ngram_range,
        stop_words=stop_words,
        min_df=min_df,
        max_features=max_features
    )
    tfidf_matrix = vectorizer.fit_transform(texts)
    features = vectorizer.get_feature_names_out()
    if return_matrix:
        return tfidf_matrix, features, texts
    else:
        avg_tfidf = np.asarray(tfidf_matrix.mean(axis=0)).ravel()
        keywords = sorted(zip(features, avg_tfidf), key=lambda x: x[1], reverse=True)
        return keywords

def nmf_topic_modeling(
    tfidf_matrix,
    feature_names,
    n_topics=5,
    n_top_words=10,
    random_state=0
):
    nmf_model = NMF(n_components=n_topics, random_state=random_state)
    W = nmf_model.fit_transform(tfidf_matrix)
    H = nmf_model.components_
    topics = []
    for topic_idx, topic in enumerate(H):
        top_keywords = [feature_names[i] for i in topic.argsort()[:-n_top_words-1:-1]]
        topics.append((topic_idx+1, top_keywords))
    return nmf_model, W, topics

def assign_and_show_sample_reviews(
    df, W, reviews_idx, n_topics=5, n_samples=3, text_col='review'
):
    topic_assignment = W.argmax(axis=1)
    df.loc[reviews_idx, 'topic'] = topic_assignment
    for topic in range(n_topics):
        print(f"\nTopic #{topic+1} sample reviews:")
        sample = df[df['topic'] == topic][text_col].head(n_samples)
        for review in sample:
            print(f"- {review}")

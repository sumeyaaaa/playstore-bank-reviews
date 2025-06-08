import re
import string
import spacy

# Load spaCy English model (make sure you've downloaded it!)
nlp = spacy.load("en_core_web_sm")

def clean_lemmatize(text: str) -> str:
    """
    Clean and lemmatize input text:
    - Lowercase
    - Remove punctuation and digits
    - Remove stopwords
    - Lemmatize tokens
    """
    # Lowercase and basic cleaning
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Lemmatization
    doc = nlp(text)
    return " ".join(
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and token.lemma_.isalpha()
    )

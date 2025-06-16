import spacy
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Preprocessing function
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

# Load FAQs from JSON
with open('flight_booking_faqs.json', 'r', encoding='utf-8') as f:
    faqs = json.load(f)

# Extract questions
faq_questions = [faq['question'] for faq in faqs]

# Preprocess all questions
preprocessed_questions = [preprocess(q) for q in faq_questions]

# Vectorize the questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

# Train Nearest Neighbors model
model = NearestNeighbors(n_neighbors=1, metric='cosine')
model.fit(X)

# Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("faq_data.json", "w", encoding="utf-8") as f:
    json.dump(faqs, f, indent=2)

import gradio as gr
import pickle
import json
import spacy
from sklearn.neighbors import NearestNeighbors

# Load saved components
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("faq_data.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)

# Load SpaCy for preprocessing
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

# Chatbot response function
def chatbot_response(user_input):
    processed = preprocess(user_input)
    vec = vectorizer.transform([processed])
    dist, idx = model.kneighbors(vec)
    if dist[0][0] < 0.5:  # adjust threshold as needed
        return faqs[idx[0][0]]['answer']
    else:
        return "Sorry, I don't understand the question."

# Custom CSS for the Gradio interface
custom_css = """
    .gradio-container {
        max-width: 800px !important;
        margin: 0 auto !important;
    }
    .gradio-interface {
        padding: 20px !important;
    }
    .gradio-input {
        font-size: 16px !important;
    }
    .gradio-output {
        font-size: 16px !important;
    }
"""

# Create Gradio Interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(
        label="Ask me anything about flight booking",
        placeholder="Type your question here...",
        lines=2
    ),
    outputs=gr.Textbox(
        label="Response",
        lines=4
    ),
    title="Flight Booking Assistant",
    description="I'm here to help you with all your flight booking questions!",
    theme=gr.themes.Soft(),
    css=custom_css,
    flagging_mode="never"
)

# Launch the interface in the background
if __name__ == "__main__":
    interface.launch(share=False, inbrowser=False)

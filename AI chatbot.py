import nltk
import spacy
import random
from nltk.tokenize import word_tokenize

# Download NLTK tokenizer
nltk.download()
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses for common questions
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm good, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "your name": ["I'm a chatbot created to assist you!", "You can call me ChatBot!"],
    "thank you": ["its ok"]
}

def chatbot_response(user_input):
    """Process user input and return an appropriate response."""
    
    # Convert input to lowercase and tokenize
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    # Check for predefined responses
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])

    # Use spaCy for Named Entity Recognition (NER)
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Check for a location
            return f"Oh, {ent.text} is a great place!"

    # If no match is found, return a generic response
    return "I'm not sure about that, but I'm learning new things every day!"

# Run the chatbot in a loop
print("🤖 Chatbot: Hello! Type 'exit' to stop.")
while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("🤖 Chatbot: Goodbye!")
        break
    response = chatbot_response(user_text)
    print(f"🤖 Chatbot: {response}")
    
    

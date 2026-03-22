responses = {
    "greeting": "Hello! How can I help?",
    "bye": "Goodbye!"
}

def generate(intent):
    return responses.get(intent, "I don't understand")
intents = {
    "greeting": ["hi", "hello"],
    "bye": ["bye", "goodbye"]
}

def classify(text):
    for intent, words in intents.items():
        if text.lower() in words:
            return intent
    return "unknown"
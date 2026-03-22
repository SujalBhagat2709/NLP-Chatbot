from intent_classifier import classify
from response_generator import generate

while True:
    user = input("You: ")
    intent = classify(user)
    response = generate(intent)
    print("Bot:", response)
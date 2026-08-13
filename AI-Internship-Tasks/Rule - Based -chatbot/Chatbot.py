print("=" * 40)
print("Welcome to Rule-Based Chatbot")
print("Type 'bye' to exit.")
print("=" * 40)

name = input("Enter your name: ")
print(f"Hello {name}! Nice to meet you.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I am RuleBot, a simple AI chatbot.")

    elif "python" in user:
        print("Bot: Python is a programming language used in AI and Data Science.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    
    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
        
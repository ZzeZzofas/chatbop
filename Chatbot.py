def chatbot():
    responses = {"hi": "Hello!", "how are you": "I'm a bot, I'm always good!", "bye": "Goodbye!"}
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        elif user_input == "exit":
            break
        else:
            print("Bot: I don't understand.")
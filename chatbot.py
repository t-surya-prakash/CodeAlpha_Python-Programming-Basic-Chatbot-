def get_response(message):
    """Return a predefined reply for the user's message."""
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple Python chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' for ideas."


def main():
    print("=== SIMPLE CHATBOT ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()

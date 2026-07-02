"""
Task 4: Basic Chatbot
A simple rule-based chatbot that responds to predefined user inputs.
"""


def get_response(user_input):
    """Return a predefined reply based on the user's input."""
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm a simple rule-based chatbot."
    elif user_input == "help":
        return "You can say: hello, how are you, what is your name, or bye."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I know."


def chatbot():
    """Run the chatbot loop until the user says 'bye'."""
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    chatbot()
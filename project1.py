import random

conversation_history = {'user': [], 'bot': []}


# Greetings message
def greet():
    responses = ["Hello! I'm a simple chatbot. How can I assist you today?",
                 "Hi there! What can I help you with?",
                 "Hey! Feel free to ask me anything."]
    return random.choice(responses)

# Responses to basic questions
def respond(question):
    question = question.lower()
    if "how are you" in question:
        return "I'm just a bot, so I'm always ready to assist you!"
    elif "what can you do" in question:
        return "I can answer questions, provide information, or just have a chat with you."
    elif "who created you" in question:
        return "I was created by Rutuja."
    elif "how does" in question:
        return "Could you please specify what you'd like to know more about?"
    elif "are you a real person" in question:
        return "No, I'm a chatbot programmed to assist you."
    else:
        return "I'm sorry, I don't understand that question."

# Farewell message
def farewell():
    return "Goodbye! Feel free to come back if you have more questions."

# Main function to handle the conversation
def chat():
    print(greet())
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "bye":
            print(farewell())
            break
        else:
            bot_response = respond(user_input)
            print(bot_response)
            # Store conversation history
            conversation_history['user'].append(user_input)
            conversation_history['bot'].append(bot_response)

# Start the conversation
chat()

# Print conversation history
print("\nConversation History:")
for user_msg, bot_msg in zip(conversation_history['user'], conversation_history['bot']):
    print("User: ", user_msg)
    print("Bot: ", bot_msg)

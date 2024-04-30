import random

conversation_history = {'user': [], 'bot': []}


# Responses to basic questions
def respond(question):
    question = question.lower()
    if "admission procedure" in question:
        return "To begin the admission process, you need to fill out our online application form."
    elif "application form" in question:
        return "You will find the form on the university website under 'New Admissions' section."
    elif "fee structure" in question:
        return "Our fee structure varies depending on the program. Please provide your desired program for more details. \nFor Computer Science and Information Technology - 4Lpa \nFor Electrical - 3Lpa \nFor Civil ad Mechanical - 3Lpa"
    elif "admission begin" in question:
        return "After the results of the entrance test, the selected students will get an email regarding further procedure and timelines."
    elif "okay" in question:
        return "Is there any other query I can help you with?"
    else:
        return "For this concern, please contact the admin office."

# Farewell message
def farewell():
    return "Thank you for your time."

# Main function to handle the conversation
def chat():
    print("Welcome! How may I assist you today?")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "exit":
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

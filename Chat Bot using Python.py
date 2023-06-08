from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Main program loop
print("Chatbot: Hello, how can I assist you today?")

while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        break

    bot_response = get_bot_response(user_input)
    print("Chatbot:", bot_response)
import re
import random
from nltk.chat.util import Chat, reflections

def default_response():
    responses = [
        "I'm not sure I understand. Could you rephrase that?",
        "Interesting! Can you tell me more?",
        "Let's discuss something else. What else is on your mind?",
        "I see. How does that make you feel?"
    ]
    return random.choice(responses)

# Define a set of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What's on your mind?", "Hey! How's it going?"]
    ],
    [
        r"what is your name\??",
        ["I am a chatbot created to chat with you. What's your name?", "I'm your friendly chatbot. Do you have a name?"]
    ],
    [
        r"how are you\??",
        ["I'm just a bunch of code, but I'm functioning perfectly. How about you?", "I'm doing well! How can I help you today?"]
    ],
    [
        r"(.*) (created|made) (you|this bot)\??",
        ["I was created by a developer using Python! Do you want to learn how to build one like me?", "Someone skilled in programming brought me to life."]
    ],
    [
        r"(.*) weather (.*)",
        ["I'm not connected to live weather data, but it looks great in here!", "I'm unsure about the weather, but I hope it's nice where you are!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! It was nice chatting with you."]
    ]
]

# Create a chatbot instance using NLTK's Chat class
class SimpleChatbot(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)

    def converse(self, quit="quit"):
        print("Chatbot: Hi! Type 'bye', 'exit', or 'quit' to end the conversation.")
        user_input = ""
        while user_input.lower() not in ["bye", "exit", "quit"]:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "exit", "quit"]:
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print(f"Chatbot: {default_response()}")

# Instantiate the chatbot and start the conversation
if __name__ == "__main__":
    chatbot = SimpleChatbot(pairs, reflections)
    chatbot.converse()

import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hi there"]
    ],
    [
        r"what is your name?",
        ["My name is RoBot", "I'm RoBot"]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about You?", "I am fine"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that!"]
    ],
    [
        r"quit",
        ["Bye-bye! Take care."]
    ],     
    [   r"",
        ["Sorry"]           
             
    ],
]


def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()
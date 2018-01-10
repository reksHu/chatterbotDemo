# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database="./lowConfidence.db",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65

        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

# Train the chat bot with a few responses
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)
while True:
    try:
        inputVal= input()
        responseVal = bot.get_response((inputVal))
        print(responseVal)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break
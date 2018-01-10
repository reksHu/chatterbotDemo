from chatterbot import ChatBot
chatbot = ChatBot(
    'myBot',
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    trainer= 'chatterbot.trainers.ChatterBotCorpusTrainer',

    database="./greeting.db",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response",
            'default_response': 'I am sorry, but I do not understand.'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ]
)

chatbot.train("chatterbot.corpus.english.greetings")
response = chatbot.get_response("Hello")

print(response)

while True:
    try:
        sentence= input()
        response = chatbot.get_response(sentence)
        print(response)
    except(KeyboardInterrupt, EOFError,SystemExit):
        break
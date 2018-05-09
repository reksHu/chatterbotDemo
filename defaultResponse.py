from chatterbot import  ChatBot
chatbot = ChatBot(
    'myBot',
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    trainer= 'chatterbot.trainers.ChatterBotCorpusTrainer',
    database="./greeting.db",
    read_only=True,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response",
            'default_response': 'I am sorry, but I do not understand.'
        }
    ]
)

chatbot.train("chatterbot.corpus.english.greetings")
while True:
    sentence = input("ask your question:")
    result = chatbot.get_response(sentence)
    print(result)
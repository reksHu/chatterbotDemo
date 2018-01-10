from chatterbot import ChatBot
from chatterbot.comparisons import jaccard_similarity
# some error occured, not working.
# "statement_comparison_function": "chatterbot.comparisons.JaccardSimilarity", not working
chatbot = ChatBot(
    'ramdonChatter',
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    trainer= 'chatterbot.trainers.ChatterBotCorpusTrainer',
    database="./random.db",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"

        }
    ],
    statement_comparison_function = jaccard_similarity
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
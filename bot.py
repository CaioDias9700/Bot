from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("bottest001", tagger_language=ENGSM)
dialogo = [
    "oi",
    "eai",

]
trainer = ListTrainer(chatbot)
trainer.train(dialogo)
while True:
    mensagem = input()
    if mensagem == "sair":
        break;
    resposta = chatbot.get_response(mensagem)
    print(resposta)

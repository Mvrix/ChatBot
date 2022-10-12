from urllib import response
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# arrumar bug en compatibilidade
from spacy.cli import download
download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

# CODIGO COMEÇA AQUI tagger_language=ENGSM


chatbot = ChatBot("BotMariu")

talk = [
    "Coe",
    "Eai, tranquilo? ",
    "Suave po",
    "Qual a boa?",
    "Nada não, só lol mesmo",
    "E a mina?",
    "Foi de nanos na mae",
    "Complicado..."
]

# resposta do chat:
trainer = ListTrainer(chatbot)
trainer.train(talk)


while True:
    talk = input("Mande uma mensagem para o chatbot:")
    if talk == "parar":
        break
    resposta = chatbot.get_response(talk)
    print(resposta)

# falar com o bot manual:

chatbot.get_response("e a mina?")

# limpar armazenamento

chatbot.storage.drop()

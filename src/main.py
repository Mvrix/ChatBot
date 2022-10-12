from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# arrumar bug en compatibilidade
from spacy.cli import download

download("en_core_web_sm")


# class ENGSM:

#   ISO_639_1 = 'en_core_web_sm'

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
    "Foda..."
]

trainer = ListTrainer(chatbot)
trainer.train(talk)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def answer(message):
    bot = ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('C:\\Users\\Vanna\\Downloads\\Compressed\\jowithme\\greetings.yml')
    reply = bot.get_response(message)
    return reply
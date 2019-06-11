from fbchat import Client, log
from fbchat.models import *
import apiai, codecs, json
from user import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def answer(message):
    bot = ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('greetings.yml')
    reply = bot.get_response(message)
    return reply

class Jarvis(Client):



    # Connect to dialogflow
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "Your Client Access Token"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de'  # Default : English
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        # Mark message as read
        self.markAsRead(author_id)

        # Print info on console
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        # Establish conn
        self.apiaiCon()

        # Message Text
        msgText = message_object.text
        log.info(msgText)
        reply= answer(msgText)
        # Request query/reply for the msg received
        # self.request.query = msgText

        # Get the response which is a json object
        # response = self.request.getresponse()

        # Convert json object to a list
        # reader = codecs.getdecoder("utf-8")
        # obj = json.load(reader(response))

        # Get reply from the list
        # reply = obj['result']['fulfillment']['speech']
        # reply = 'Hello'
        # Send message
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            # self.send('hello')

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)


# Create an object of our class, enter your email and password for facebook.
client = Jarvis(user, password)

# Listen for new message
client.listen()

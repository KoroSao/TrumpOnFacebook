import fbchat
from fbchat import Client
from fbchat.models import *
from getpass import getpass
import time
import wget
from fbchat import log
from fbchat import *
from phrase import *
import random

conv_id = 4194894710583853
"""
echo = False
# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if message_object.text == "/repeat on" and thread_type == ThreadType.GROUP:
            echo = True
            return echo
        elif message_object.text == "Remove me!" and thread_type == ThreadType.GROUP:
            echo = False
            return echo
        if echo == True:
            self.markAsDelivered(thread_id, message_object.uid)
            self.markAsRead(thread_id)

            log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

            # If you're not the author, echo
            if author_id != self.uid:
                self.send(message_object, thread_id='4194894710583853', thread_type=ThreadType.GROUP)

client = EchoBot("yellingtrump@nerfus.fr", "Fidji123_")
"""

class RemoveBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # We can only kick people from group chats, so no need to try if it's a user chat
        if message_object.text == "Remove me!" and thread_type == ThreadType.GROUP:
            log.info("{} will be removed from {}".format(author_id, thread_id))
            self.removeUserFromGroup(author_id, thread_id=thread_id)
        elif message_object.text == "/color change viking" and thread_type == ThreadType.GROUP:
            client.changeThreadColor(ThreadColor.VIKING, thread_id=conv_id)
        elif message_object.text == "/color change blue" and thread_type == ThreadType.GROUP:
            client.changeThreadColor(ThreadColor.MESSENGER_BLUE, thread_id=conv_id)
        elif message_object.text == "/color change gold" and thread_type == ThreadType.GROUP:
            client.changeThreadColor(ThreadColor.GOLDEN_POPPY, thread_id=conv_id)
        elif message_object.text == "/color change red" and thread_type == ThreadType.GROUP:
            client.changeThreadColor(ThreadColor.RADICAL_RED, thread_id=conv_id)
        elif message_object.text.lower() == "bonjour trump" and thread_type == ThreadType.GROUP:
            dict = client.fetchUserInfo(author_id)
            nom = str(dict.get(author_id))
            sep = "name='"
            sep2 = "'"
            nom = nom.split(sep, 1)[1]
            nom = nom.split(sep2, 1)[0]
            print(nom)
            client.send(Message(text='Bonjour ' + nom), thread_id=conv_id, thread_type=ThreadType.GROUP)
        elif (message_object.text.lower() == "ça va trump ?" or message_object.text.lower() == "ca va trump ?" or message_object.text.lower() == "ca va trump?" or message_object.text.lower() == "ça va trump?") and thread_type == ThreadType.GROUP:
            dict = client.fetchUserInfo(author_id)
            nom = str(dict.get(author_id))
            sep = "name='"
            sep2 = "'"
            nom = nom.split(sep, 1)[1]
            nom = nom.split(sep2, 1)[0]
            print(nom)
            i = random.randint(0,len(howAreUAnswer) -1)
            client.send(Message(text=howAreUAnswer[i] + ", et toi " + nom + " ?"), thread_id=conv_id, thread_type=ThreadType.GROUP)
        elif (message_object.text.lower() == "tu veux ma photo ?" or message_object.text.lower() == "tu veux ma photo?") and thread_type == ThreadType.GROUP:
            dict = client.fetchUserInfo(author_id)
            url = str(dict.get(author_id))
            sep = "photo='"
            sep2 = "'"
            url = url.split(sep, 1)[1]
            url = url.split(sep2, 1)[0]
            i = random.randint(0,len(myPictureAnswer) -1)
            client.sendRemoteImage(url, message=myPictureAnswer[i], thread_id=conv_id, thread_type=ThreadType.GROUP)
        elif message_object.text.lower() == "/citation" and thread_type == ThreadType.GROUP:
            dict = client.fetchUserInfo(author_id)
            nom = str(dict.get(author_id))
            sep = "name='"
            sep2 = "'"
            nom = nom.split(sep, 1)[1]
            nom = nom.split(sep2, 1)[0]
            i = random.randint(0,len(citationAnswer) -1)
            client.send(Message (text = "Tu sais " + nom + " : " + citationAnswer[i]), thread_id=conv_id, thread_type=ThreadType.GROUP)
        elif message_object.text.lower() == "/party" and thread_type == ThreadType.GROUP:
            client.send(Message (text = "3"), thread_id=conv_id, thread_type=ThreadType.GROUP)
            time.sleep(1)
            client.send(Message (text = "2"), thread_id=conv_id, thread_type=ThreadType.GROUP)
            time.sleep(1)
            client.send(Message (text = "1"), thread_id=conv_id, thread_type=ThreadType.GROUP)
            time.sleep(0)
            client.send(Message (text = "Let's party !"), thread_id=conv_id, thread_type=ThreadType.GROUP)
            client.sendLocalImage('giphy.gif', message=None, thread_id=conv_id, thread_type=ThreadType.GROUP)
            for loop in range(3):
                client.changeThreadColor(ThreadColor.VIKING, thread_id=conv_id)
                time.sleep(0.3)
                client.changeThreadColor(ThreadColor.GOLDEN_POPPY, thread_id=conv_id)
                time.sleep(0.3)
                client.changeThreadColor(ThreadColor.RADICAL_RED, thread_id=conv_id)
                time.sleep(0.3)
        elif message_object.text.lower() == "/help" and thread_type == ThreadType.GROUP:
            dict = client.fetchUserInfo(author_id)
            nom = str(dict.get(author_id))
            sep = "name='"
            sep2 = "'"
            nom = nom.split(sep, 1)[1]
            nom = nom.split(sep2, 1)[0]
            client.send(Message (text = nom + ", je suis encore en développement 👨🏽‍💻. Voici les commandes que tu peux utiliser : \n- /color change pour changer la couleur 🌈\n- /citation pour une citation aléatoire 📜\n- /party pour enflammer le dance floor🔥🕺🏿🔥\n- 'ça va trump?' pour me demander comment je vais 😀\n- 'tu veux ma photo' pour te juger 📸"), thread_id=conv_id, thread_type=ThreadType.GROUP)
            
        else:
            # Sends the data to the inherited onMessage, so that we can still see when a message is recieved
            super(RemoveBot, self).onMessage(
                author_id=author_id,
                message_object=message_object,
                thread_id=thread_id,
                thread_type=thread_type,
                **kwargs
            )

client = RemoveBot(mail, pwd)

client.listen()

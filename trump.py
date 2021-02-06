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
import os

conv_id = 4194894710583853

def getNameFromDict(author_id):
    dict = client.fetchUserInfo(author_id)
    nom = str(dict.get(author_id))
    sep = "name='"
    sep2 = "'"
    nom = nom.split(sep, 1)[1]
    nom = nom.split(sep2, 1)[0]
    return nom

def getPhotoUrlFromDict(author_id):
    dict = client.fetchUserInfo(author_id)
    url = str(dict.get(author_id))
    sep = "photo='"
    sep2 = "'"
    url = url.split(sep, 1)[1]
    url = url.split(sep2, 1)[0]
    return url

def getFriendStatusFromDict(author_id):
    dict = client.fetchUserInfo(author_id)
    isFriend = str(dict.get(author_id))
    sep = "is_friend="
    sep2 = ","
    isFriend = isFriend.split(sep, 1)[1]
    isFriend = isFriend.split(sep2, 1)[0]
    return isFriend

class RemoveBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        words = message_object.text.split()
        #ROOT OF COMMANDS
        if words[0].lower() == "/trump":
            if len(words) == 1 :
                client.send(Message (text = "Hello, my name is Trump, you can use '/trump help' to have more information."), thread_id=thread_id, thread_type=thread_type)
            #FIRST WORD TESTING
            elif len(words) >= 1 :

                #DISPLAY HELP METHOD
                if words[1].lower() == "help" and len(words) <= 2:
                    client.send(Message (text = "Je suis encore en développement 👨🏽‍💻. Voici les commandes que tu peux utiliser : \n- /color change pour changer la couleur 🌈\n- /citation pour une citation aléatoire 📜\n- /party pour enflammer le dance floor🔥🕺🏿🔥\n- 'ça va trump?' pour me demander comment je vais 😀\n- 'tu veux ma photo' pour te juger 📸"), thread_id=thread_id, thread_type=thread_type)
                
                #TRIGGER PARTY MODE
                elif words[1].lower() == "party" and len(words) <= 2:
                    client.send(Message (text = "3"), thread_id=thread_id, thread_type=thread_type)
                    time.sleep(1)
                    client.send(Message (text = "2"), thread_id=thread_id, thread_type=thread_type)
                    time.sleep(1)
                    client.send(Message (text = "1"), thread_id=thread_id, thread_type=thread_type)
                    time.sleep(0)
                    client.send(Message (text = "Let's party !"), thread_id=thread_id, thread_type=thread_type)
                    client.sendLocalImage('giphy.gif', message=None, thread_id=thread_id, thread_type=thread_type)
                    for loop in range(3):
                        client.changeThreadColor(ThreadColor.VIKING, thread_id=thread_id)
                        time.sleep(0.3)
                        client.changeThreadColor(ThreadColor.GOLDEN_POPPY, thread_id=thread_id)
                        time.sleep(0.3)
                        client.changeThreadColor(ThreadColor.RADICAL_RED, thread_id=thread_id)
                        time.sleep(0.3)
                
                #Display citation
                elif words[1].lower() == "citation" and len(words) <= 2:
                    i = random.randint(0,len(citationAnswer) -1)
                    client.send(Message (text = "Tu sais " + getNameFromDict(author_id) + " : " + citationAnswer[i]), thread_id=thread_id, thread_type=thread_type)

                #Mood
                elif words[1].lower() == "mood" and len(words) <= 2:
                    i = random.randint(0,len(howAreUAnswer) -1)
                    client.send(Message(text=howAreUAnswer[i] + ", et toi " + getNameFromDict(author_id) + " ?"), thread_id=thread_id, thread_type=thread_type)
               
                #Bonjour
                elif words[1].lower() == "bonjour" and len(words) <= 2:
                    client.send(Message(text='Bonjour ' + getNameFromDict(author_id) + " !"), thread_id=thread_id, thread_type=thread_type)

                #TU VEUX MA PHOTO ?
                elif words[1].lower()=="tuveuxmaphoto?" and len(words) <= 2:
                    i = random.randint(0,len(myPictureAnswer) -1)
                    client.sendRemoteImage(getPhotoUrlFromDict(author_id), message=myPictureAnswer[i], thread_id=thread_id, thread_type=thread_type)

                elif words[1].lower() == "friendlist" and len(words) <= 2:
                    users = client.fetchAllUsers()
                    client.send(Message(text="J'ai " + str(len(users)) + " amis! Voici mes amis :"), thread_id=thread_id, thread_type=thread_type)
                    for user in users :
                        client.send(Message(text=user.name), thread_id=thread_id, thread_type=thread_type)
                
                elif words[1].lower() == "addfriend" and len(words) <= 2:
                    if getFriendStatusFromDict(author_id) == "True" :
                        client.send(Message(text="Nous sommes déjà ami " + getNameFromDict(author_id) + " !"), thread_id=thread_id, thread_type=thread_type)
                    else:
                        client.send(Message(text="Je vous ai envoyé une demande d'ami " + getNameFromDict(author_id) + " !"), thread_id=thread_id, thread_type=thread_type)
                        client.friendConnect(author_id)

                elif words[1].lower() == "pay" and len(words) <= 2:
                    client.send(Message(text="Merci de nous aider à développer la puissance de Trump:\n https://www.paypal.com/pools/c/8rNji9c0x8 "), thread_id=thread_id, thread_type=thread_type)

                elif words[1].lower() == "sing" and len(words) <= 2:
                    i = random.randint(0,len(singAnswer) -1)
                    client.send(Message(text="Voici mon dernier single:\n" + singAnswer[i]), thread_id=thread_id, thread_type=thread_type)


                else:
                     client.send(Message (text = "No such command found"), thread_id=thread_id, thread_type=thread_type)


 
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

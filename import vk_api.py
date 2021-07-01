import vk_api
import os 
from vk_api.longpoll import VkLongPoll,VkEventType

vk_session = vk_api.VkApi(token = 'af1bc7208642ea4bf574e95bac97962840c2beda7b8156cae01021abe9bcc49f9fa23f59bf966abbfb7c5')
session_api = vk_session.get_api()
longpoll = VkLongPoll (vk_session)

def sender(id, text):
    vk_session.method("messages.send", {"user_id" : id, "message" : text, "random_id" : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == "топ чел":
                sender(id, "ьоооо")

            elif msg == "ха":
                sender(id, "лох")

            elif msg == "а":
                sender(id, "б")

token = os.environ.get('BOT_TOKEN')
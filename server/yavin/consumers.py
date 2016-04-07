import json
from channels import Group


# Connected to websocket.connect
def ws_add(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    msg = json.loads(message.content['text'])
    Group("chat").send({
        "text": "[{}] {}".format(msg['user'], msg['text'])
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

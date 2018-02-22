#coding:utf-8
# Last modified: 2016-12-01 18:06:48
# by zhangdi http://jondy.net/
from django.utils import timezone
from django.conf import settings
import time
import json

def ws_open(message):
  pass
  #print message.items()
  #Group('chat').add(message.reply_channel)

def ws_message(message):
  # ASGI WebSocket packet-received and send-packet message types
  # both have a "text" key for their textual data.
  message.reply_channel.send({
    "text": message.content['text'],
  })

def dev_import(message):
  cmd = json.loads(message.content['text'])
  print "0000000000000000000000000",cmd
  message.reply_channel.send({
    "text": json.dumps(rs),
  })


#coding:utf-8
# Last modified: 2016-08-31 11:11:11
# by zhangdi http://jondy.net/
from channels.routing import route
from webapp.agent.consumer import ws_message

channel_routing = [
    #route('send-invite',send_invite),
   # route("websocket.receive", 'webapp.dbman.consumer.index', path=r'^/index/$'),
    #route("websocket.receive", 'webapp.dbman.consumer.status_table', path=r'^/status_table/$'),
   # route("websocket.receive", 'webapp.dbman.consumer.status_group', path=r'^/status_group/$'),
    route("websocket.receive", 'webapp.agent.consumer.dev_import', path=r'^/import/$'),
    #route("websocket.receive", 'webapp.dbman.consumer.status_bridge', path=r'^/status_bridge/$'),
    #route("websocket.connect", 'webapp.dbman.consumer.ws_open'),

    #route("websocket.receive", 'webapp.dbman.consumer.ws_message'),
]

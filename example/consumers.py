# This example uses WebSocket consumer, which is synchronous, and so
# needs the async channel layer functions to be converted.
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept() 
        async_to_sync(self.channel_layer.group_add)("users", self.channel_name)
        self.user = self.scope["user"]
        print("User "+self.user)
        async_to_sync(self.channel_layer.group_send)({
                'text': json.dumps({
                    'username': self.user.username,
                    'is_logged_in': True
                    }),
                })

        def disconnect(self, close_code): 
            async_to_sync(self.channel_layer.group_discard)("users", self.channel_name)
            async_to_sync(self.channel_layer.group_send)({
                'text': json.dumps({
                    'username': self.user.username,
                    'is_logged_in': True
                    }),
                })
           
            self.close()




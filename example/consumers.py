# This example uses WebSocket consumer, which is synchronous, and so
# needs the async channel layer functions to be converted.
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer): 

    def connect(self): 

        self.room_group_name = 'chat_users' 

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
        )

        self.accept() 

         # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username,
                'is_logged_in': True 
            }
        )






    def disconnect(self, close_code): 
        # Send message to room group

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username,
                'is_logged_in': False 
            }
        )


        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name) 
       

  


    # Receive message from room group
    def chat_message(self, event):


        # Send message to WebSocket
        self.send(text_data=json.dumps({
                    'username': event['username'],
                    'is_logged_in': event['is_logged_in']
                    }))

           




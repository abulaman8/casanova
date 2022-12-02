import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class AdminConsumer(WebsocketConsumer):
    def connect(self):
        
        self.room_group_name = "admin_room"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        print(self.channel_name)

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        lat = text_data_json["lattitude"]
        lng = text_data_json["longitude"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "co-ords",
                 "lattitide": lat,
                 "longitude": lng
                  }
        )
        

    # Receive message from room group
    def chat_message(self, event):
        lat = event["lattitude"]
        lng = event["longitude"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type':'websocket.send',
            "lattitude": lat,
            "longitude": lng
        }))
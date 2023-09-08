# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        event = {"type": "chat.message", "message": message}
        await self.channel_layer.group_send(
            self.room_group_name, event
        )

    async def chat_message(self, event):
        message = event["message"]
        json_message = json.dumps({"message": message})
        await self.send(text_data = json_message)


class DrawConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_group_name = "test"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, data):
        # print("data", type(data['message']))
        event = {"type": "chat.message", "message": data["message"]}
        await self.channel_layer.group_send(
            self.room_group_name, event
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send_json(message)
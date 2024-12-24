import json
from channels.generic.websocket import AsyncWebsocketConsumer

class websocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pass

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def send_message(self, event):
        pass

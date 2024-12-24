form django.urls import path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/game/$', consumers.websocketConsumer.as_asgi()),
]

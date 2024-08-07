from django.urls import path

from general.consumers import UserConsumer, MessageConsumer


websocket_urlpatterns = [
    path("ws/", UserConsumer.as_asgi()),
    path('ws/message/', MessageConsumer.as_asgi()),
]

from django.urls import re_path

from . import consumers

from channels.routing import URLRouter

websocket_urlpatterns = URLRouter([
    # re_path(r"ws/student/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),

])

# urlpatterns = [
#     re_path(r"(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),

# ]
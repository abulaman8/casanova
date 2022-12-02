from django.urls import path

from . import consumers

from channels.routing import URLRouter

websocket_urlpatterns = URLRouter([
    # re_path(r"ws/student/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path("admin_room/", consumers.AdminConsumer.as_asgi()),

])
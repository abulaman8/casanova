# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "casanova.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from student.routing import websocket_urlpatterns as student_ws_urls
from cadmin.routing import websocket_urlpatterns as cadmin_ws_urls


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(
               [
                   path('ws/student/', student_ws_urls),
                   path('ws/admin/', cadmin_ws_urls),
                ]
                # student.routing.websocket_urlpatterns
                ))
        ),
    }
)
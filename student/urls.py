
from django.urls import path
from .views import MyTokenObtainPairView, get_cameras, register_user


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('get-cameras/', get_cameras),
    path('register/', register_user),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

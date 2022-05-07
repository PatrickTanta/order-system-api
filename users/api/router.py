from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApiViewSet, UserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='user', viewset=UserApiViewSet
)

urlpatterns = [
    path('auth/me/', UserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
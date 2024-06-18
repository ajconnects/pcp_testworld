from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterProgrammerView, RegisterClientView, LogoutAndBlacklistRefreshTokenForUserView, ObtainTokenPairWithEmailView

urlpatterns = [
    path('register/programmer/', RegisterProgrammerView.as_view(), name='register_programmer'),
    path('register/client/', RegisterClientView.as_view(), name='register_client'),
    path('login/', ObtainTokenPairWithEmailView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
]
from django.urls import path
from .views import RegisterView, UserDetailView, ProgrammerProfileView, ClientProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('programmer-profile/', ProgrammerProfileView.as_view(), name='programmer_profile'),
    path('client-profile/', ClientProfileView.as_view(), name='client_profile'),
]

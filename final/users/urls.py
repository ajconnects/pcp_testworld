from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView, RefreshAPIView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('refresh', RefreshAPIView.as_view()), #part2
    path('logout', LogoutView.as_view()),
]

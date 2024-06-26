from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'programmers', ProgrammerViewSet, basename='programmer')
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path("", include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('public-search/', PublicProgrammerSearchView.as_view(), name='public-programmer-search'),
]
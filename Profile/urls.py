from django.urls import path
from .views import custom_login, custom_logout, check_auth

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('api/check-auth/', check_auth, name='check_auth'),
]
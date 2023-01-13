from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import (
    signupapiview,
    UserLoginApiview,
    LogoutApiview,
    profileListapiview,
    ProfileUpdateApiview,
    UserUpdateApiview,
    UserListapiview,
    Changepasswordapiview,
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',signupapiview.as_view(), name = 'user-signup'),
    path('login/',UserLoginApiview.as_view(), name = 'user-login'),
    path('logout/',LogoutApiview.as_view(),name = 'user-logout'),
    path('profile/', profileListapiview.as_view(), name = 'profile-list'),
    path('profile/<int:pk>/',ProfileUpdateApiview.as_view(), name = ' profile-update'),
    path('user/',UserListapiview.as_view(), name = 'user-list'),
    path('user/<int:pk>/',UserUpdateApiview.as_view(), name = 'user-update'),
    path('changepassword',Changepasswordapiview.as_view(), name = 'change-password'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

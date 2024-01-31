from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('', index, name='index')
]
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('task/', index, name='index')
]
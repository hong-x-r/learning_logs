"""URL patterns for users"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Defualt auth urls cover login, logout
    path( '', include( 'django.contrib.auth.urls' ) ),
    path( 'register/', views.register, name = 'register' ),
]


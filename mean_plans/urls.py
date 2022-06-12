"""Definitions of URL patterns for mean_plans"""
from django.urls import path
from . import views

app_name = 'mean_plans'
urlpatterns = [
    #Home page
    path( 'mp/', views.index_mp, name = 'index_mp' ),
]


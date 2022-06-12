"""URL patterns for learning_logs_app"""
from django.urls import path
from . import views

app_name = 'learning_logs_app'
urlpatterns = [
    path( '', views.index, name = 'index' ),
    path( 'index/', views.index, name = 'index' ),
    path( 'topics/', views.topics, name = 'topics' ),
    path( 'topic/<int:topic_id>/', views.topic, name = 'topic' ),
    path( 'new_topic/', views.new_topic, name = 'new_topic' ),
    path( 'new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry' ),
    path( 'new_entry_any/', views.new_entry_any, name = 'new_entry_any' ),
    path( 'edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry' ),
]


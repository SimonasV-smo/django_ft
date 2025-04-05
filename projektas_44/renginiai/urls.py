from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('events/', views.event_list_view, name='event_list'),
    path('join/<int:event_id>/', views.join_event_view, name='join_event'),
]
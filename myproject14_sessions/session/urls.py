from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_session, name='create_session'),
    path('get/', views.get_session, name='get_session'),
    path('delete/', views.delete_session, name='delete_session'),
]
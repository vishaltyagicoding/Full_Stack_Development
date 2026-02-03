from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.index, name='about'),
    path('submit/', views.submit, name='submit'),
]
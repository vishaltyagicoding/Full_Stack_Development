from .views import *
from django.urls import path
app_name = 'todo'
urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_create, name='task_add'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('toggle/<int:pk>/', task_toggle_complete, name='task_toggle_complete'),
]
from django.urls import path
from .views import *

urlpatterns = [

    path('', dashboard, name='dashboard'),

    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/update/<int:id>/', category_update, name='category_update'),
    path('categories/delete/<int:id>/', category_delete, name='category_delete'),

    path('priorities/', priority_list, name='priority_list'),
    path('priorities/create/', priority_create, name='priority_create'),
    path('priorities/update/<int:id>/', priority_update, name='priority_update'),
    path('priorities/delete/<int:id>/', priority_delete, name='priority_delete'),

    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/update/<int:id>/', task_update, name='task_update'),
    path('tasks/delete/<int:id>/', task_delete, name='task_delete'),

    path('subtasks/', subtask_list, name='subtask_list'),
    path('subtasks/create/', subtask_create, name='subtask_create'),
    path('subtasks/update/<int:id>/', subtask_update, name='subtask_update'),
    path('subtasks/delete/<int:id>/', subtask_delete, name='subtask_delete'),

    path('notes/', note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/update/<int:id>/', note_update, name='note_update'),
    path('notes/delete/<int:id>/', note_delete, name='note_delete'),
    
]
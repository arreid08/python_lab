from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_list),
    path('groups/', views.group_list, name = 'group_list'),
    path('groups/<int:id>', views.group_detail, name = 'group_detail'),
    path('groups/create', views.group_create, name = 'group_create'),
    path('groups/<int:id>/edit', views.group_update, name = 'group_update'),
    path('groups/<int:id>/delete', views.group_delete, name = 'group_delete'),
    path('tasks/<int:id>/edit', views.task_update, name = 'task_update'),
    path('tasks/<int:id>/delete', views.task_delete, name = 'task_delete'),
]
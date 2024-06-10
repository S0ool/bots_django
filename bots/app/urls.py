from django.contrib import admin
from django.urls import path

from app.views import index, add_robot, robot_info, delete_robot, edit_robot

urlpatterns = [
    path('', index, name='index'),
    path('add_robot', add_robot, name='add_robot'),
    path('robot_info/<int:robot_id>', robot_info, name='robot_info'),
    path('edit_robot/<int:robot_id>', edit_robot, name='edit_robot'),
    path('delete_robot/<int:robot_id>', delete_robot, name='delete_robot'),

]

from django.contrib import admin
from django.urls import path

from app.views import index, add_robot, robot_info, delete_robot, edit_robot, categories, add_category, category_info, \
    edit_category, delete_category, add_shop, shops, shop_info, edit_shop, delete_shop

urlpatterns = [
    path('', index, name='index'),
    path('add_robot', add_robot, name='add_robot'),
    path('robot_info/<int:robot_id>', robot_info, name='robot_info'),
    path('edit_robot/<int:robot_id>', edit_robot, name='edit_robot'),
    path('delete_robot/<int:robot_id>', delete_robot, name='delete_robot'),


    path('categories', categories, name='categories'),
    path('add_category', add_category, name='add_robot'),
    path('category_info/<int:category_id>', category_info, name='category_info'),
    path('edit_category/<int:category_id>', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>', delete_category, name='delete_category'),

    path('shops', shops, name='shops'),
    path('add_shop', add_shop, name='add_shop'),
    path('shop_info/<int:shop_id>', shop_info, name='shop_info'),
    path('edit_shop/<int:shop_id>', edit_shop, name='edit_shop'),
    path('delete_shop<int:shop_id>', delete_shop, name='delete_shop'),

]

from django.urls import path, re_path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('items/', views.items, name = 'items'),
    path('create_item/', views.create_item, name = 'create_item'),
    path('create_brand/', views.create_brand, name= 'create_brand'),
    path('view_item/<int:id>/', views.view_item, name='view_item'),
    path('update_item/<int:id>/', views.update_item, name='update_item'),
    path('update_item/<int:id>/delete/', views.delete_item, name='delete_item'),
    path('upload_pics/', views.upload_pics, name='upload_pics'),
    path('control/', views.control, name = 'control'),
    path('make_list/', views.make_list, name = 'make_list'),
    path('collect_list/', views.collect_list, name = 'make_list'),

]
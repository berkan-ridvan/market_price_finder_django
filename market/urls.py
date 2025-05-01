from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/items/', views.get_items, name='get_items'),
    path('api/items/create/', views.create_item, name='create_item'),
    path('api/items/<int:item_id>/update/', views.update_item, name='update_item'),
    path('api/items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
] 

from django.urls import path
from . import views
urlpatterns=[
    path('restaurant',views.restaurant,name='restaurant'), 
    path('restaurants',views.restaurants,name='restaurants'),
    path('createRestaurant',views.createRestaurant,name='createRestaurant'),
    path('insertRestaurant',views.insertRestaurant,name='insertRestaurant'),
    path('readRes/',views.readRestaurant,name='readRestaurant'),
    path('deleteRestaurant/<int:id>/', views.deleteRestaurant, name='deleteRestaurant'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateRestaurant/<int:id>/', views.updateRestaurant, name='updateRestaurant'),
]
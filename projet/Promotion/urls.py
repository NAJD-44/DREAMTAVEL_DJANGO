from django.urls import path
from . import views
urlpatterns=[
    path('promotion',views.promotion,name='promotion'), 
    path('promotions',views.promotions,name='promotions'),
    path('createPromotion',views.createPromotion,name='createPromotion'),
    path('insertPromotion',views.insertPromotion,name='insertPromotion'),
     path('readProm/',views.readPromotion,name='readPromotion'),
    path('deletePromotion/<int:id>/', views.deletePromotion, name='deletePromotion'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updatePromotion/<int:id>/', views.updatePromotion, name='updatePromotion'),
]
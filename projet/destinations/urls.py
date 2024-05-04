from django.urls import path
from . import views
urlpatterns=[
    path('destination',views.destination,name='destination'), 
    path('destinations',views.destinations,name='destinations'),
    path('createDestination/',views.createDestination,name='createDestination'),
    path('insertDestination',views.insertDestination,name='insertDestination'),
    path('readDes/',views.readDestination,name='readDestination'),
    path('deleteDestination/<int:id>/', views.deleteDestination, name='deleteDestination'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateDestination/<int:id>/', views.updateDestination, name='updateDestination'),
]
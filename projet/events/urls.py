from django.urls import path
from . import views
urlpatterns=[
    path('event',views.event,name='event'), 
    path('events',views.events,name='events'),
    path('createEvent',views.createEvent,name='createEvent'),
    path('insertEvent',views.insertEvent,name='insertEvent'),
     path('readEve/',views.readEvent,name='readEvent'),
    path('deleteEvent/<int:id>/', views.deleteEvent, name='deleteEvent'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateEvent/<int:id>/', views.updateEvent, name='updateEvent'),
]
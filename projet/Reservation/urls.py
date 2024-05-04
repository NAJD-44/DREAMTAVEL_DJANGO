from django.urls import path
from . import views
urlpatterns=[
    path('reservation',views.reservation,name='reservation'), 
    path('reservations',views.reservations,name='reservations'),
    path('createReservation',views.createReservation,name='createReservation'),
    path('insertReservation',views.insertReservation,name='insertReservation'),
     path('readRes/',views.readReservation,name='readReservation'),
    path('deleteReservation/<int:id>/', views.deleteReservation, name='deleteReservation'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateReservation/<int:id>/', views.updateReservation, name='updateReservation'),
]
from django.urls import path
from . import views
urlpatterns=[
    path('touriste',views.touriste,name='touriste'), 
    path('touristes',views.touristes,name='touristes'),
    path('signup',views.signup,name='signup'),
    path('insertTouriste',views.insertTouriste,name='insertTouriste'),
    path('readTou/',views.readTouriste,name='readTouriste'),
    path('deleteTouriste/<int:id>/', views.deleteTouriste, name='deleteTouriste'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateTouriste/<int:id>/', views.updateTouriste, name='updateTouriste'),
]
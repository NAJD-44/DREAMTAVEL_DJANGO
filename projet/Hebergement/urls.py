from django.urls import path
from . import views
urlpatterns=[
    path('hebergement',views.hebergement,name='hebergement'), 
    path('hebergements',views.hebergements,name='hebergements'),
    path('createHebergement',views.createHebergement,name='createHebergement'),
    path('insertHebergement',views.insertHebergement,name='insertHebergement'),
     path('readHeb/',views.readHebergement,name='readHebergement'),
    path('deleteHebergement/<int:id>/', views.deleteHebergement, name='deleteHebergement'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateHebergement/<int:id>/', views.updateHebergement, name='updateHebergement'),
]
from django.urls import path
from . import views
urlpatterns=[
    path('attraction',views.attraction,name='attraction'), 
    path('attractions',views.attractions,name='attractions'),
    path('createAttraction',views.createAttraction,name='createAttraction'),
    path('insertAttraction',views.insertAttraction,name='insertAttraction'),
    path('readAtt/',views.readAtt,name='readAtt'),
    path('deleteAttraction/<int:id>/', views.deleteAttraction, name='deleteAttraction'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateAttraction/<int:id>/', views.updateAttraction, name='updateAttraction'),
]
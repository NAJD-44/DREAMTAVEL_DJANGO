from django.urls import path
from . import views
urlpatterns=[
    path('experience',views.experience,name='experience'), 
    path('experiences',views.experiences,name='experiences'),
    path('createExperience',views.createExperience,name='createExperience'),
    path('insertExperience',views.insertExperience,name='insertExperience'),
    path('readExperience/',views.readExperience,name='readExperience'),
    path('deleteExperience/<int:id>/', views.deleteExperience, name='deleteExperience'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateExperience/<int:id>/', views.updateExperience, name='updateExperience'),
]
from django.urls import path
from . import views
urlpatterns=[
    path('transport',views.transport,name='transport'), 
    path('transports',views.transports,name='transports'),
    path('createTransport',views.createTransport,name='createTransport'),
    path('insertTransport',views.insertTransport,name='insertTransport'),
    path('readTra/',views.readTransport,name='readTransport'),
    path('deleteTransport/<int:id>/', views.deleteTransport, name='deleteTransport'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('updateTransport/<int:id>/', views.updateTransport, name='updateTransport'),
]
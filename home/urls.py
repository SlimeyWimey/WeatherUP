
from . import views 
import connexion.views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', connexion.views.register, name='register'),
]

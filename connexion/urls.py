from django.urls import path
import connexion
import home
from . import views
from home import views


urlpatterns = [
    path('login/', views.login_page, name='login' ),
    path('logout/', connexion.views.logout, name='logout'),
    path('pageutilisateur/', views.utilisateur_page,name='pageutilisateur'),
    path('home/', home.views.index, name='index'),
]


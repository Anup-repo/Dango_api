from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('api/teamapi', views.team, name='teamdetails'),
    path('api/teamvsteam', views.teamVteam, name='teamvteam'),
    path('api/allrecords', views.allrecords, name='allrecords'),
]
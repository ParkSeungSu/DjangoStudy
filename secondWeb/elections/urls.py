from django.contrib import admin
from django.urls import path
from . import views

app_name = 'elections'
urlpatterns = [
    path('',views.index,name='home'),
    path('areas/<str:area>/',views.areas,name='areas'),
    path('areas/<str:area>/results',views.results,name='results'),
    path('polls/<int:poll_id>',views.polls,name='polls'),
    path('candidates/<str:name>/',views.candidates,name='candidates'),
    
]


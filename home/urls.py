from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('about', views.about, name="about"),
    path('', views.index, name='index'),

]

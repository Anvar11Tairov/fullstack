from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('exam/', views.exam),
    path('service/', views.service),
    path('services/<int:id>', views.getService),
    path('postuser/', views.postuser),
    path('login/', views.login),
    path('team/', views.team)
]

from django.contrib import admin
from django.urls import path, include
from . import views
from . import dashboard

urlpatterns = [
    path('', views.index, name='home_view'),
]

"""Defines URL patterns for clients."""

from django.urls import path
from django.conf.urls import url

from .import views

app_name = 'clients'
urlpatterns = [
    #Company Page
    path('', views.office, name = 'office'),
    path('office/', views.office, name = 'office'),
    path('office/<int:client_id>/', views.office, name = 'office'),
    ]
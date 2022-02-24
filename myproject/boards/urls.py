from django.urls import path

from . import views

urlpatterns = [
    path('', views.homex, name='home'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('current', views.current, name='current'),
    path('latest', views.latest, name='latest'),
]

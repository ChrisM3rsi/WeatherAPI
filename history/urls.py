from django.urls import path

from . import views

urlpatterns = [
    path('<int:timestamp>', views.history, name='history'),
]
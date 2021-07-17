from django.urls import path
from . import views

urlpatterns = [
    path('<str:project>', views.builder_), #Builder Application
]
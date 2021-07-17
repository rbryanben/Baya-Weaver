from django.urls import path
from . import views
from django.conf import settings
from .views import theme_upload

urlpatterns = [
    path('<str:project>', views.builder_), #Builder Application
    path('theme', theme_upload,name="theme"), #uploadtheme test Application
]

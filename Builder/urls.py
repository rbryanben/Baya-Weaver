from django.urls import path
from . import views

urlpatterns = [
    path('project/<str:project>/', views.builder_), #Builder Application
    path('create-project/',views.create_project_), #Create Project
    path('get-project-template/<str:id>/',views.get_project_template), #Get project template
]
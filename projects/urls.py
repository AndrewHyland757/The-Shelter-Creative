from django.urls import path
from . import views


urlpatterns = [
    
    path('<slug:project_slug>/', views.project, name="project"),
    
]
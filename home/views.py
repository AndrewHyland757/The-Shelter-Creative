from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project


def home(request):
    """
    Renders home page
    """

    projects = Project.objects.all()

    context = {
     "projects": projects,
    }
    template = "home/home.html"
  
    return render(request, template, context)

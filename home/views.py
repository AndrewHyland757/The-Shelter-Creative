from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    """
    Renders home page.
    """
    template = "home/home.html"
  
    return render(request, template)
from django.shortcuts import render
from projects.models import Project


def handler404(request, exception):
    """ 
    Error Handler 404 - Page Not Found 
    """

    projects = Project.objects.all()

    context = {
     "projects": projects,
    }

    return render(request, "404.html", context=context, status=404)

    




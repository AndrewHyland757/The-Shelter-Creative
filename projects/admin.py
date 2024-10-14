from django.contrib import admin
from .models import Project, Service, Template, Section, ProjectPage


admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Section)

admin.site.register(Template)
admin.site.register(ProjectPage)

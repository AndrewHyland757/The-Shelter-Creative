from django.contrib import admin
from .models import Project, MainService, Service, Template, Section, Section1, Section2, ProjectPage


admin.site.register(Section2)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(MainService)
admin.site.register(Section)
admin.site.register(Section1)
admin.site.register(Template)
admin.site.register(ProjectPage)

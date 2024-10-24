from django.contrib import admin
from .models import Project, Service, Template, Section, ProjectPage


admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Template)


class SectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('project', 'template','html_description_name', 'use_custom_html', 'use_custom_css', 'change_header_color', 'change_text_color', 'video_file'),
        }),
        ('Custom HTML/CSS', {
            'classes': ('collapse',),  # This will collapse the section by default
            'fields': ('custom_html', 'custom_css'),
        }),
        ('Change header color', {
            'classes': ('collapse',),  # This will collapse the section by default
            'fields': ('new_header_color', 'new_header_color_hover', 'new_header_color_tablet', 'new_header_color_hover_tablet', 'new_header_color_mobile', 'new_header_color_hover_mobile'),
        }),
        ('Change text color', {
            'classes': ('collapse',),  # This will collapse the section by default
            'fields': ('new_text_color', 'new_text_color_tablet', 'new_text_color_mobile'),
        }),
        # Description 1
        ('Project Description Text', {
            'classes': ('collapse',),  # Collapses this section by default
            'fields': ('project_description_1', 'project_description_2'),
        }),
      
      # Image 1
        ('Image 1', {
            'classes': ('collapse',),  # Collapses this section by default
            'fields': ('img_1', 'img_1_tablet', 'img_1_mobile', 'img_1_description'),
        }),
        # Image 2
        ('Image 2', {
            'classes': ('collapse',),
            'fields': ('img_2', 'img_2_tablet', 'img_2_mobile', 'img_2_description'),
        }),
        # Image 3
        ('Image 3', {
            'classes': ('collapse',),
            'fields': ('img_3', 'img_3_tablet', 'img_3_mobile', 'img_3_description'),
        }),
        # Image 4
        ('Image 4', {
            'classes': ('collapse',),
            'fields': ('img_4', 'img_4_tablet', 'img_4_mobile', 'img_4_description'),
        }),
        # Image 5
        ('Image 5', {
            'classes': ('collapse',),
            'fields': ('img_5', 'img_5_tablet', 'img_5_mobile', 'img_5_description'),
        }),
        # Image 6
        ('Image 6', {
            'classes': ('collapse',),
            'fields': ('img_6', 'img_6_tablet', 'img_6_mobile', 'img_6_description'),
        }),
        # Image 7
        ('Image 7', {
            'classes': ('collapse',),
            'fields': ('img_7', 'img_7_tablet', 'img_7_mobile', 'img_7_description'),
        }),
    )

admin.site.register(Section, SectionAdmin)



@admin.register(ProjectPage)
class ProjectPageAdmin(admin.ModelAdmin):
    """
    Filter the section options based on the project associated with the ProjectPage
    """
    list_select_related = ('project',)
    raw_id_fields = ('project',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name.startswith('section_'):
            if request.resolver_match.kwargs.get('object_id'):
                project_page = ProjectPage.objects.get(pk=request.resolver_match.kwargs['object_id'])
                kwargs["queryset"] = Section.objects.filter(project=project_page.project)
            elif request.POST.get('project'):
                kwargs["queryset"] = Section.objects.filter(project_id=request.POST['project'])
            else:
                kwargs["queryset"] = Section.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
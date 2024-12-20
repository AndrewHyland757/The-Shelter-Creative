import os
from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Max
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from cloudinary.api import resources


def get_unique_image_name(instance, filename):
    """
    Generates image name using the project company name,
    allowing Cloudinary to handle the uniqueness by appending identifiers if needed.
    """
    project_slug = slugify(instance.project.company)
    base_filename = f"The-Shelter-Creative-{project_slug}"
    file_extension = os.path.splitext(filename)[-1]

    # Return the full path for the image
    return f"project_images/{instance.project.slug}/{base_filename}{file_extension}"


def get_project_image_upload_to(instance, filename):
    """
    Generates image name using the project company name,
    allowing Cloudinary to handle the uniqueness by appending identifiers if needed.
    """
    if instance.project and instance.project.slug:
        project_folder = slugify(instance.project.slug)
        return f'project_images/{project_folder}/{filename}'
    else:
        return f'project_images/default/{filename}'


class Template(models.Model):
    """
    Model for the html templates.
    """
    template_name = models.CharField(max_length=255)
    html_content = models.TextField(null=False)
    css_content = models.TextField(null=True, blank=True)
    template_description = models.TextField(null=True)

    class Meta:
        ordering = ['template_name']

    def __str__(self):
        return f"{self.template_name}"


class Service(models.Model):
    """
    Model for the list of services.
    """
    service_name = models.CharField(max_length=200)

    def __str__(self):
        return self.service_name


class Project(models.Model):
    """
    Model for the projects.
    """
    company = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    main_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='main_service')
    services = models.ManyToManyField(Service, related_name='secondary_services')  # Corrected: ManyToManyField does not accept null=False
    list_position = models.IntegerField(unique=True)
    list_image = models.ImageField(upload_to='project_images/list_images', blank=True, null=True)

    class Meta:
        ordering = ['list_position']

    def __str__(self):
        return f"{self.list_position} - {self.company}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.company)
        super().save(*args, **kwargs)


class SectionCleanMixin:
    def clean(self):
        # Validate custom HTML and CSS fields
        if self.use_custom_html and not self.custom_html:
            raise ValidationError("Custom HTML must be provided if 'Use Custom HTML' is checked.")

        if self.use_custom_css and not self.custom_css:
            raise ValidationError("Custom CSS must be provided if 'Use Custom CSS' is checked.")

        # Validation: If template is null, ensure custom HTML/CSS usage
        if self.template is None:
            if not self.use_custom_html:
                raise ValidationError("If no template is selected, 'Use Custom HTML' must be True.")
            if not self.use_custom_css:
                raise ValidationError("If no template is selected, 'Use Custom CSS' must be True.")
            if not self.custom_html:
                raise ValidationError("Custom HTML must be provided if no template is selected.")
            if not self.custom_css:
                raise ValidationError("Custom CSS must be provided if no template is selected.")


class Section(SectionCleanMixin, models.Model):
    """
    Model for any other sections in the project page. A custom html template can be used
    or a template from the templates model. Up to six images can be used and an
    optional description text.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

    # Custom html and css
    use_custom_html = models.BooleanField(default=False)
    custom_html = models.TextField(blank=True, null=True)
    html_description_name = models.CharField(max_length=255, blank=True, null=True)
    use_custom_css = models.BooleanField(default=False)
    custom_css = models.TextField(blank=True, null=True)

    # Optional text and services
    project_description_1 = models.TextField(blank=True, null=True)
    project_description_2 = models.TextField(blank=True, null=True)

    # Color changes for header
    change_header_color = models.BooleanField(default=False)
    new_header_color = models.CharField(max_length=200, blank=True, null=True)
    new_header_color_hover = models.CharField(max_length=200, blank=True, null=True)
    new_header_color_tablet = models.CharField(max_length=200, blank=True, null=True)
    new_header_color_hover_tablet = models.CharField(max_length=200, blank=True, null=True)
    new_header_color_mobile = models.CharField(max_length=200, blank=True, null=True)
    new_header_color_hover_mobile = models.CharField(max_length=200, blank=True, null=True)

    # Color changes for company/service text
    change_text_color = models.BooleanField(default=False)
    new_text_color = models.CharField(max_length=200, blank=True, null=True)
    new_text_color_tablet = models.CharField(max_length=200, blank=True, null=True)
    new_text_color_mobile = models.CharField(max_length=200, blank=True, null=True)

    # Video file
    video_file = CloudinaryField(resource_type='video', folder="media/project_videos", use_filename=True,
                                 unique_filename=False, blank=True, null=True)

    # Images and descriptions for up to 7 images with dynamic upload path
    img_1 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_1_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_1_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_1_description = models.TextField(blank=True, null=True)

    img_2 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_2_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_2_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_2_description = models.TextField(blank=True, null=True)

    img_3 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_3_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_3_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_3_description = models.TextField(blank=True, null=True)

    img_4 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_4_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_4_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_4_description = models.TextField(blank=True, null=True)

    img_5 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_5_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_5_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_5_description = models.TextField(blank=True, null=True)

    img_6 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_6_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_6_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_6_description = models.TextField(blank=True, null=True)

    img_7 = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_7_tablet = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_7_mobile = models.ImageField(upload_to=get_unique_image_name, blank=True, null=True)
    img_7_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.project.company}: {self.html_description_name if self.html_description_name  else self.template.template_name}"

    class Meta:
        verbose_name = "Project Page Section"
        verbose_name_plural = "Project Page Sections"


class ProjectPage(models.Model):
    """
    Model for the project page. this consists of all sections associated with the project.
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    section_1 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_1')
    section_2 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_2')
    section_3 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_3')
    section_4 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_4')
    section_5 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_5')
    section_6 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_6')
    section_7 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_7')
    section_8 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_8')
    section_9 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_9')
    section_10 = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name='section_10')

    def __str__(self):
        return f"Project page - {self.project.company}"

    def get_absolute_url(self):
        return f'/{self.project.slug}/'

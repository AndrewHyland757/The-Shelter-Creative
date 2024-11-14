# project/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import ProjectPage

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ProjectPage.objects.all()

    def location(self, obj):
        return f"{settings.SITE_URL}/{obj.slug}/"

        

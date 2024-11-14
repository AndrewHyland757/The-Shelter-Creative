from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import HomeSitemap
from projects.sitemaps import ProjectSitemap


handler404 = "the_shelter.views.handler404"

sitemaps = {
    'home': HomeSitemap,
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("project/", include("projects.urls")),
]


if not settings.DEBUG:
    urlpatterns += [
        path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
             name='django.contrib.sitemaps.views.sitemap'),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


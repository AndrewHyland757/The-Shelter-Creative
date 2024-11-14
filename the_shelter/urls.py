from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("project/", include("projects.urls")),
]

handler404 = "the_shelter.views.handler404"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

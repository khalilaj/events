from django.conf.urls import include, url
from django.contrib import admin

from conference_api import settings

urlpatterns = [
    url(r"^admin/", admin.site.urls, 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r"^", include("app.urls")),
]

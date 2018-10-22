from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include("conference.urls")),
    url(r"^", include("event.urls")),
    url(r"^", include("event_attendant.urls")),
    url(r"^", include("event_feedback.urls")),
    url(r"^", include("event_speaker.urls")),
]

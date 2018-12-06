from django.conf.urls import include, url
from .user import views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    url(r"^login/", views.LoginView.as_view()),
    url(r"^register/", views.RegistrationView.as_view()),
    url(r"^user/", include("app.user.urls")),
    url(r"^session/", include("app.session.urls")),
    url(r"^conference/", include("app.conference_details.urls")),
    url(r"^tag/", include("app.tag.urls")),
    url(r"^conference_attendants/", include("app.conference_attendants.urls")),
    url(r"^conference_feedback/", include("app.conference_feedback.urls")),
    url(r"^session_attendants/", include("app.session_attendants.urls")),
    url(r"^session_speaker/", include("app.session_speaker.urls")),
    url(r"^session_feedback/", include("app.session_feedback.urls")),
    url(r"^session_material/", include("app.session_material.urls")),
    url(r"^session_forum_topic/", include("app.session_forum_topic.urls")),
    url(r"^session_forum_responses/", include("app.session_forum_responses.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

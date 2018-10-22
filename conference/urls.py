from django.conf.urls import include, url
from .user import views

urlpatterns = [
    url(r"^login/", views.LoginView.as_view()),
    url(r"^register/", views.RegistrationView.as_view()),
    url(r"^user/", include("conference.user.urls")),
    url(r"^event/", include("conference.event.urls")),
    url(r"^event_attendant/", include("conference.event_attendant.urls")),
    url(r"^event_speaker/", include("conference.event_speaker.urls")),
    url(r"^event_feedback/", include("conference.event_feedback.urls")),
    url(r"^conference/", include("conference.conference.urls")),
]

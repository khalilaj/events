from django.conf.urls import include, url
from .user import views

urlpatterns = [
    url(r"^login/", views.LoginView.as_view()),
    url(r"^register/", views.RegistrationView.as_view()),
    url(r"^user/", include("conference.user.urls")),
    url(r"^conference/", include("conference.conference.urls")),
]

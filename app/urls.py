from django.conf.urls import include, url
from .user import views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    url(r"^login/", views.LoginView.as_view()),
    url(r"^register/", views.RegistrationView.as_view()),
    url(r"^user/", include("app.user.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

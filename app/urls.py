from django.conf.urls import include, url
from .user import views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    url(r"^api/login/", views.LoginView.as_view()),
    url(r"^api/register/", views.RegistrationView.as_view()),
    url(r"^api/user/", include("app.user.urls")),
    url(r"^api/event/", include("app.event.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

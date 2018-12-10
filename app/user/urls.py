from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^$", views.AccountRetrieveUpdateView.as_view()),
    url(r"^(?P<pk>\d+)$", views.AccountEdit.as_view(), name="edit-user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

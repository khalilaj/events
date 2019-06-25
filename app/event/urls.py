from django.conf.urls import url

from .views import ListCreate, RetrieveUpdateDestroy

urlpatterns = [
    url(r"^$", ListCreate.as_view(), name="list-create-event"),
    url( r"^(?P<pk>\d+)$", RetrieveUpdateDestroy.as_view(),name="retrieve-event",),
]
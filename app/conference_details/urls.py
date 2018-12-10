from django.conf.urls import url

from .views import ConferenceListCreate, ConferenceRetrieveUpdateDestroy

urlpatterns = [
    url(r"^$", ConferenceListCreate.as_view(), name="list-create-conference"),
    url( r"^(?P<pk>\d+)$", ConferenceRetrieveUpdateDestroy.as_view(),name="retrieve-update-conference",),
]

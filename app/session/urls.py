from django.conf.urls import url
from .views import SessionListCreate, SessionRetrieve

urlpatterns = [    
    url(r'^$', SessionListCreate.as_view(), name='list-create-session'),
    url(r'^(?P<pk>\d+)$', SessionRetrieve.as_view(), name='retrieve-update-session'),
]
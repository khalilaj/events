from django.conf.urls import url
from .views import SessionMaterialListCreate, SessionMaterialRetrieve

urlpatterns = [    
    url(r'^$', SessionMaterialListCreate.as_view(), name='list-create-session_material'),
    url(r'^(?P<pk>\d+)$', SessionMaterialRetrieve.as_view(), name='retrieve-update-session_material'),
]
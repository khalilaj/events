from django.conf.urls import url
from .views import TagListCreate, TagRetrieve

urlpatterns = [    
    url(r'^$', TagListCreate.as_view(), name='list-create-tag'),
    url(r'^(?P<pk>\d+)$', TagRetrieve.as_view(), name='retrieve-update-tag'),
]
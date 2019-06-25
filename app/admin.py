from django.contrib import admin

from .user.models import Account 
from .event.models import Event 

models = [
          Account,
          Event,
          ]

admin.site.register(models)

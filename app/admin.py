from django.contrib import admin

from .user.models import Account 


models = [
          Account,
          ]

admin.site.register(models)

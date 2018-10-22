from django.contrib import admin

from .user.models import Account
from .event.models import Event
from .event_attendant.models import EventAttendant
from .event_feedback.models import EventFeedback
from .event_speaker.models import EventSpeaker
from .conference.models import Conference


models = [Conference,
          Event,
          EventAttendant,
          EventFeedback,
          EventSpeaker,
          Account,
          ]

admin.site.register(models)

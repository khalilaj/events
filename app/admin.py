from django.contrib import admin

from .user.models import Account
from .session.models import Session
from .conference_attendants.models import ConferenceAttendants
from .session_attendants.models import SessionAttendants
from .conference_feedback.models import ConferenceFeedback
from .session_feedback.models import SessionFeedback
from .session_speaker.models import SessionSpeaker
from .session_forum_topic.models import SessionForumTopic
from .session_forum_responses.models import SessionForumResponses
from .session_material.models import SessionMaterial
from .conference_details.models import Conference
from .tag.models import Tag


models = [
          Conference,
          Session,
          Tag,
          ConferenceAttendants,
          SessionAttendants,
          SessionFeedback,
          ConferenceFeedback,
          SessionSpeaker,
          SessionForumTopic,
          SessionMaterial,
          SessionForumResponses,
          Account,
          ]

admin.site.register(models)

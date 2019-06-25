from __future__ import unicode_literals
from datetime import datetime, timedelta
import jwt
import json
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from ..core.models import StrictTimestamp


class AcountManager(BaseUserManager):
    """
    Class that extends the django BaseUserManager
    """

    def create_user(self, email, password, **kwargs):
        """
        Creates a basic user

        :return:  A valid Account
        :rtype: An Account object a
        """

        if email is None:
            raise ValueError("Email has not been provided")
        if password is None:
            raise ValueError("Password has not been provided")

        account = self.model(
         email=self.normalize_email(email), **kwargs
        )
        account.set_password(password)
        account.save()
        print(account.id)
        return account

    def create_superuser(self, email, password):

        account = self.create_user(email, password,)

        if password is None:
            raise ValueError("Superuser must have a password")

        account.is_superuser = True
        account.is_staff = True
        account.save()


class Account(AbstractBaseUser, PermissionsMixin, StrictTimestamp):
    """
    Defines the basic attributes of a user
    """

    email = models.EmailField(_("email address"), unique=True)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    profile_picture = models.FileField(verbose_name="app-logo", name=None, blank=True)
    objects = AcountManager()

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=False)

    USERNAME_FIELD = "email" 

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        """
        Defines the string representation of a User object.
        """
        return "<User firstname={}>".format(self.firstname)

    def json(self):
        """
        Defines the json representation of a User object.
        """
        return json.dumps(
            {"email": self.email, "active": self.is_active}
        )

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def token(self):
        """
         Calls the __tokenize function to tokenize the self attribute
        """
        return self._tokenize()

    def _tokenize(self):
        """
         Sets the token attribute for the user
        """
        stamp = datetime.utcnow() + timedelta(days=60)

        token = jwt.encode(
            {
                "id": self.id, 
                "email": self.email,
                "exp": stamp,
                "iat": datetime.utcnow(),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token

# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_("first_name"), max_length=30, blank=True)
    last_name = models.CharField(_("last_name"), max_length=30, blank=True)
    dirrection1 = models.CharField(_("dirrection"), max_length=30, blank=True)
    dirrection2 = models.CharField(_("dirrection2"), max_length=30, blank=True)
    town = models.CharField(_("town"), max_length=30, blank=True)
    zipcode = models.CharField(_("zipcode"), max_length=30, blank=True)
    state = models.CharField(_("state"), max_length=30, blank=True)
    country = models.CharField(_("country"), max_length=30, default=_('spain'), blank=True)
    telephone1 = models.CharField(_("telephone1"), max_length=14, blank=True)
    telephone2 = models.CharField(_("telephone2"), max_length=14, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        "Returns the first_name plus the last_name, with a space in between."
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __str__(self):
        return self.email

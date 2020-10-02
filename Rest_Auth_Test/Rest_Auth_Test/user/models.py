from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    ''' User model to store values'''
    name = models.CharField(_('name'), max_length=88, blank=True)
    email = models.EmailField(
        _('email address'), unique=True, null=True)
    is_staff = models.BooleanField(_('active'), default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s' % (self.name)
        return full_name.strip()

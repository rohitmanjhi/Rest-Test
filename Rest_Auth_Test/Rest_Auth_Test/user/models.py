from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length=88, blank=True)
    email = models.EmailField(
        _('email address'), unique=True, null=True)
    mobile = models.CharField(unique=True, max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the from retail.order.models import Order, OrderItem, Invoice, OrderSettingsfirst_name plus the last_name, with a space in between.
        '''
        full_name = '%s' % (self.name)
        return full_name.strip()
from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from . import managers 


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.email}'s account"


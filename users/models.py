from rest_framework_api_key.models import APIKey
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        max_length=254,
        unique=True,
        help_text=_("The email of the user is his username."),
    )
    api_key = models.OneToOneField(APIKey, on_delete=models.CASCADE, primary_key=True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

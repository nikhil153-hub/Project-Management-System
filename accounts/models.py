from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

ACCOUNT_TYPE = (
    ('free', 'Free'),
    ('premium', 'Premium'),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE, default='free', null=True)

    is_verified = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

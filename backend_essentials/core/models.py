from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from backend_essentials.common.manager import UserManager
from backend_essentials.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(blank=False, editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    middle_name = models.CharField()

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "gid"

    class Meta:
        db_table = "users"
        app_label = "core"
        ordering = ("-updated_at",)

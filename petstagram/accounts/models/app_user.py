from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

from petstagram.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


UserModel = get_user_model()
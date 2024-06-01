from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    first_name = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    last_name = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    is_staff = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    is_superuser = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    is_active = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    date_joined = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))
    last_login = models.EmailField(max_length=255, unique=True, verbose_name=gettext_lazy("E-mail Address"))

    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
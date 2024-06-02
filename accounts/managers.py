from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy


def email_validator(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValueError(validate_email("Please enter a valid e-mail address!"))


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            email_validator(email)
        else:
            raise ValueError(gettext_lazy("An e-mail address is required."))
        if not first_name:
            raise ValueError(gettext_lazy("The first name field is required."))
        if not last_name:
            raise ValueError(gettext_lazy("The last name field is required."))
        if not password:
            raise ValueError(gettext_lazy("The password field is required."))

        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(gettext_lazy("It's necessary that the staff field be true"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(gettext_lazy("It's necessary that the super user field be true"))

        user = self.create_user(
            email, first_name, last_name, password, **extra_fields
        )
        user.save(using=self.db)
        return user

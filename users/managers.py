from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        """
        Create and save a User with the given email and password.
        """
        if 'uid' in extra_fields and extra_fields['uid'].isnumeric():
            # facebook user may not provide the email
            email = extra_fields.pop('uid')
        extra_fields.pop('uid', None)
        if not email:
            raise ValueError(_("The Email must be set"))
        if not first_name:
            raise ValueError(_("The First name must be set"))
        if not last_name:
            raise ValueError(_("The Last name must be set"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email, password, first_name, last_name, **extra_fields
    ):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

"""
Database model for our projects user
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    PermissionsMixin, BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    """The user manager for our custom user model"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError("Email is a required Field for all users.")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model for our project"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(verbose_name="Member since", default=timezone.now)

    is_active = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        """String representation of the user model"""
        return self.email

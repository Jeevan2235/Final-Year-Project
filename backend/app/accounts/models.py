from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.api.managers import UserManager
from core.infrastructure import choices

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    gender = models.CharField(
        choices=choices.GENDER_TYPES, max_length=10, default=choices.MALE
    )
    role = models.CharField(
        choices=choices.PROFILE_TYPES, max_length=15, default=choices.CUSTOMER
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


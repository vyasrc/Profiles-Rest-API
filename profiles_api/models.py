from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""
    def create_user(self, email, name, password=None):
        """Create a new User Profile"""
        if not email:
            raise ValueError("Users must have a email address")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractUser):
    """ Database model for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of User"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of User"""
        return self.name

    def __str__(self):
        """String Representation of User"""
        return self.email

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom user model with location field
class CustomUser(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)

    # Fix reverse accessor conflict by adding unique related_names
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser, Group
from django.db import models

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('driver', 'Driver'),
    ('customer', 'Customer'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role:
            group, _ = Group.objects.get_or_create(name=self.role.capitalize())
            self.groups.set([group])

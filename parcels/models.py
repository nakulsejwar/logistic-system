from django.db import models
from django.contrib.auth import get_user_model

class Parcel(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("picked_up", "Picked Up"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
    ]

    tracking_number = models.CharField(max_length=100, unique=True)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sent_parcels")
    recipient_name = models.CharField(max_length=100)
    recipient_address = models.TextField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number

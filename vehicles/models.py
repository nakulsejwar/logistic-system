from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ("bike", "Bike"),
        ("car", "Car"),
        ("van", "Van"),
        ("truck", "Truck"),
    ]

    registration_number = models.CharField(max_length=100, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.registration_number

from django.db import models
from drivers.models import Driver
from vehicles.models import Vehicle

class Slot(models.Model):
    SLOT_STATUS_CHOICES = [
        ("available", "Available"),
        ("assigned", "Assigned"),
        ("completed", "Completed"),
    ]

    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=SLOT_STATUS_CHOICES, default="available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.time_start} to {self.time_end}"

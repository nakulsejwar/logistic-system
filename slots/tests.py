from django.test import TestCase
from .models import Slot
from drivers.models import Driver
from vehicles.models import Vehicle
from datetime import time, date

class SlotModelTest(TestCase):
    def setUp(self):
        vehicle = Vehicle.objects.create(registration_number="VH100", vehicle_type="truck", capacity=2000)
        driver = Driver.objects.create(name="Bob", phone_number="9876543210", license_number="DL12345", assigned_vehicle=vehicle)
        self.slot = Slot.objects.create(
            date=date.today(),
            time_start=time(9, 0),
            time_end=time(10, 0),
            driver=driver,
            vehicle=vehicle,
            status="assigned"
        )

    def test_slot_creation(self):
        self.assertEqual(self.slot.status, "assigned")

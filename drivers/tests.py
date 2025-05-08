from django.test import TestCase
from .models import Driver
from vehicles.models import Vehicle

class DriverModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(registration_number="TST123", vehicle_type="car", capacity=500)
        self.driver = Driver.objects.create(
            name="Alice",
            phone_number="1234567890",
            license_number="LIC123",
            assigned_vehicle=self.vehicle
        )

    def test_driver_creation(self):
        self.assertEqual(self.driver.name, "Alice")
        self.assertEqual(self.driver.assigned_vehicle.registration_number, "TST123")

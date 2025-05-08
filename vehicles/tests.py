from django.test import TestCase
from .models import Vehicle

class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            registration_number="XYZ123",
            vehicle_type="van",
            capacity=1000
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.registration_number, "XYZ123")
        self.assertTrue(self.vehicle.is_active)

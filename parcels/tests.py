from django.test import TestCase
from .models import Parcel
from django.contrib.auth import get_user_model

class ParcelModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.parcel = Parcel.objects.create(
            tracking_number="ABC123456",
            sender=self.user,
            recipient_name="John Doe",
            recipient_address="123 Test Street",
        )

    def test_parcel_creation(self):
        self.assertEqual(self.parcel.tracking_number, "ABC123456")
        self.assertEqual(self.parcel.current_status, "created")

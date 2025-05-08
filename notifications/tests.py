from django.test import TestCase
from django.conf import settings

from .models import Notification

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='This is a test notification.'
        )

    def test_notification_creation(self):
        self.assertEqual(self.notification.title, 'Test Notification')
        self.assertFalse(self.notification.is_read)

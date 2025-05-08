from django.test import TestCase
from django.conf import settings

from rest_framework.test import APIClient

class ReportsTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="admin123")
        self.client = APIClient()
        self.client.login(username="admin", password="admin123")

    def test_report_summary(self):
        response = self.client.get('/api/reports/summary/')
        self.assertEqual(response.status_code, 200)

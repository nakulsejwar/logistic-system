from django.urls import path
from .views import SystemReportView

urlpatterns = [
    path('summary/', SystemReportView.as_view(), name='system_report'),
]

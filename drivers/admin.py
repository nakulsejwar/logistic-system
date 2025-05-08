from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'license_number', 'assigned_vehicle', 'is_active')
    search_fields = ('name', 'license_number')

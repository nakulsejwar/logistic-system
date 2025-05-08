from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'vehicle_type', 'capacity', 'is_active')
    search_fields = ('registration_number',)

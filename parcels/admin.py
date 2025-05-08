from django.contrib import admin
from .models import Parcel

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender', 'recipient_name', 'current_status', 'created_at')
    search_fields = ('tracking_number', 'recipient_name')

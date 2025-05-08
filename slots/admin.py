from django.contrib import admin
from .models import Slot

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time_start', 'time_end', 'driver', 'vehicle', 'status')
    list_filter = ('status', 'date')

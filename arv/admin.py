from django.contrib import admin
from .models import ARVAvailability

class ARVAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "clinic", "arv_availability", "last_updated")
    list_filter = ("arv_availability", "last_updated")
    search_fields = ("clinic__name",)

admin.site.register(ARVAvailability, ARVAvailabilityAdmin)

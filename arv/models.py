from django.db import models

class ARVAvailability(models.Model):
    Availability_CHOICES = [
        ("available", "Available"),
        ("not available", "Not available"),
    ]

    clinic = models.ForeignKey("center.Center", on_delete=models.CASCADE, related_name="arv_availabilities")
    arv_availability = models.CharField(max_length=20, choices=Availability_CHOICES)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ARV Availability at {self.clinic}: {self.arv_availability}"

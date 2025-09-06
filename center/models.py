import uuid
from django.db import models


class Center(models.Model):
    CENTER_TYPE_CHOICES = [
        ('clinic', 'Clinic'),
        ('counseling_center', 'Counseling Center'),
    ]

    center_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    center_name = models.CharField(max_length=100)
    center_type = models.CharField(max_length=100, choices=CENTER_TYPE_CHOICES)
    image_path = models.URLField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=20)
    operational_status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    operating_hours = models.DateTimeField()

    def __str__(self):
        return self.center_name



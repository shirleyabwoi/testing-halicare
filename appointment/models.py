from django.db import models
from users.models import AppUser
from center.models import Center
from services.models import Service

# Create your models here.
class Appointment(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    booking_status= models.CharField(max_length=100)
    appointment_date = models.DateField()
   

    def __str__(self):
        return f"Appointment {self.id}" 
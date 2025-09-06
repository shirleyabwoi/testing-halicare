import uuid 
from django.db import models


class Service (models.Model):
    service_id =  models.UUIDField(primary_key=True)
    center_id = models.ForeignKey(Centers, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    is_active = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.service_name

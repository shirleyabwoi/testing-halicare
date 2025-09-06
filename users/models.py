from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
class AppUser(models.Model):
    USER_TYPE_CHOICES = [
        ('Patient', 'Patient'),
        ('Clinician', 'Clinician'),
    ]
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_"): 
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})"
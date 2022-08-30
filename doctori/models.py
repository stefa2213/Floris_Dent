from datetime import datetime
from django.db import models


class Doctor(models.Model):
    nume_doctor = models.CharField(max_length=40)
    specializare = models.CharField(max_length=50)
    experienta = models.IntegerField()
    email = models.EmailField(blank=True, max_length=50)
    descriere = models.TextField(blank=True, max_length=300)
    varsta = models.IntegerField()
    image = models.ImageField(upload_to='images/doctori/', null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nume_doctor}'

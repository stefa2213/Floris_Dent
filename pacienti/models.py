from django.db import models


class Pacient(models.Model):
    nume = models.CharField(max_length=50)
    varsta = models.IntegerField(blank=True)
    telefon = models.CharField(blank=True, max_length=25)
    email = models.EmailField(blank=True, max_length=50)
    detalii = models.TextField(blank=True, max_length=500)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nume} - telefon:{self.telefon}'


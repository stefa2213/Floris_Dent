from django.db import models
from doctori.models import Doctor


class Programari(models.Model):
    prenume = models.CharField(max_length=30)
    nume = models.CharField(max_length=30)
    varsta = models.IntegerField()
    numar_telefon = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True, max_length=50)
    ora_programare = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.prenume}, {self.nume} - {self.ora_programare}, la doctorul: {self.doctor}'

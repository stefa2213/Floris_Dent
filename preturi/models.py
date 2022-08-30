from django.db import models


class Pret(models.Model):
    nume_serviciu = models.CharField(max_length=50)
    pret_serviciu = models.IntegerField()
    detalii = models.CharField(blank=True, max_length=100)
    durata = models.CharField(max_length=20)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nume_serviciu}, {self.pret_serviciu}'

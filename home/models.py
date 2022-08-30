from django.db import models


class Mesaj(models.Model):

    nume = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    numar_telefon = models.CharField(blank=True, max_length=20)
    subiect = models.CharField(max_length=30)
    mesaj = models.TextField(max_length=500)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nume} - {self.subiect}'
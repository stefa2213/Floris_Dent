# Generated by Django 4.1 on 2022-10-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('varsta', models.IntegerField(blank=True)),
                ('telefon', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('detalii', models.TextField(blank=True, max_length=500)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
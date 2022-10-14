# Generated by Django 4.1 on 2022-08-27 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_doctor', models.CharField(max_length=40)),
                ('specializare', models.CharField(max_length=50)),
                ('experienta', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('descriere', models.TextField(blank=True, max_length=300)),
                ('varsta', models.IntegerField()),
                ('image', models.ImageField(default='static/images/logo_profile_doc.jpg', upload_to='images/doctori')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
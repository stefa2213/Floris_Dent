# Generated by Django 4.1 on 2022-08-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctori', '0005_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/doctori/'),
        ),
    ]
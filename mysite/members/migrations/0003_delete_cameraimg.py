# Generated by Django 4.2.4 on 2023-08-08 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_personattendance_delete_markpresence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CameraImg',
        ),
    ]
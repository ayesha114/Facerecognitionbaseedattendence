# Generated by Django 4.2.4 on 2023-08-08 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturedimage',
            name='attendance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.attendance'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_capturedimage_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capturedimage',
            name='attendance',
        ),
        migrations.AddField(
            model_name='capturedimage',
            name='student',
            field=models.ForeignKey(null=True, on_delete=models.CASCADE, to='members.Student'),
            preserve_default=False,
        ),
    ]
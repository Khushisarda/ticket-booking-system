# Generated by Django 5.2 on 2025-04-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_show_available_seats_alter_show_total_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='image_url',
        ),
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='show_images/'),
        ),
    ]

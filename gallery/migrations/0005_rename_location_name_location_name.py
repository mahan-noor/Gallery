# Generated by Django 3.2.3 on 2021-05-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210517_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
    ]

# Generated by Django 5.2.3 on 2025-07-08 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodshare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodpost',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='foodpost',
            name='image3',
        ),
    ]

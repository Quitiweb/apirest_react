# Generated by Django 2.1.5 on 2020-03-10 15:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_auto_20200219_1242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Profile',
        ),
    ]

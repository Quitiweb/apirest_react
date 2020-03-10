# Generated by Django 2.1.5 on 2020-03-10 16:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200310_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='user',
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ManyToManyField(limit_choices_to={'is_superuser': False}, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
    ]

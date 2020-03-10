# Generated by Django 2.1.5 on 2020-03-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200310_1707'),
        ('profiles', '0004_auto_20200310_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='owner',
        ),
        migrations.AddField(
            model_name='profile',
            name='device',
            field=models.ManyToManyField(related_name='profiles', to='users.Device'),
        ),
    ]

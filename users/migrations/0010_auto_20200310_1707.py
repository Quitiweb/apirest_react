# Generated by Django 2.1.5 on 2020-03-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200310_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='user',
        ),
        migrations.AddField(
            model_name='logs',
            name='device',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='users.Device'),
            preserve_default=False,
        ),
    ]
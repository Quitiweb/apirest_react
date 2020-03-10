# Generated by Django 2.1.5 on 2020-03-10 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191202_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('remoteLog', models.BooleanField(default=False)),
                ('MACAddress', models.CharField(default='', max_length=100)),
                ('configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Configuration')),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='MACAddress',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='configuration',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='remoteLog',
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_superuser': False}, on_delete=django.db.models.deletion.CASCADE, related_name='maquinas', to=settings.AUTH_USER_MODEL),
        ),
    ]

from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import RegexValidator

MED_LENGTH = 500
MAX_LENGTH = 1500


class SubscriptionType(models.Model):
    type = models.CharField(max_length=MED_LENGTH)
    description = models.TextField(max_length=MAX_LENGTH, blank=True)

    def __str__(self):
        return self.type


# Será una tabla con unos 20 o 30 campos (aún por definir)
class Configuration(models.Model):
    fields = models.IntegerField(default=1)

    def __str__(self):
        return self.fields


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Formato: '+999999999'. Max 15 dígitos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=MED_LENGTH, blank=True)
    personal_info = models.TextField(max_length=MAX_LENGTH, blank=True)
    subscription_type = models.ForeignKey('SubscriptionType', on_delete=models.SET_NULL, null=True, blank=True)
    payed = models.BooleanField(default=False, blank=True)
    configuration = models.ForeignKey('Configuration', on_delete=models.SET_NULL, null=True, blank=True)
    remoteLog = models.BooleanField(default=False)
    MACAddress = models.CharField(max_length=100, default='')

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Logs(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='logs',
                             limit_choices_to={'is_superuser': False})
    timestamp = models.DateTimeField(default=now)
    data = models.CharField(max_length=MAX_LENGTH, blank=True)
    notes = models.TextField(max_length=MAX_LENGTH, blank=True)

    class Meta:
        verbose_name_plural = 'Logs'

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S") + hyphen(self.user.username)


def hyphen(field):
    return (' - ' + field) if field is not '' else ''

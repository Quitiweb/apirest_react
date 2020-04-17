from django.db import models
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20, blank=True, default='')
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # owner = models.ForeignKey('users.CustomUser', related_name='profiles', on_delete=models.CASCADE)
    device = models.ManyToManyField('users.Device', related_name='profiles')

    objects = models.Model

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

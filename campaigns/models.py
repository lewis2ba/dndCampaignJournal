import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)


class Session(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    description = models.CharField(max_length=300)
    def __int__(self):
        return self.number


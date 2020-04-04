from django.db import models

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateTimeField('date published')


class Session(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    description = models.CharField(max_length=300)


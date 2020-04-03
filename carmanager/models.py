from django.db import models
from datetime import datetime


class CarManager(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20,blank=False)
    phone_3 = models.CharField(max_length=20,blank=False)
    email = models.CharField(max_length=200)
    age_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    rating = models.IntegerField()
    social = models.CharField(max_length=50)
    def __str__(self):
        return self.name

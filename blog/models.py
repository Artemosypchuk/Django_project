from django.db import models
from datetime import datetime


class Blog(models.Model):
    author_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    car_id = models.IntegerField()
    text_area = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Whrite_Blog(models.Model):
    author_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    text_area = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/blog/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.title
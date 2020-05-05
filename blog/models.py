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

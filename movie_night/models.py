from datetime import datetime

from django.db import models


# Create your models here.

class Event(models.Model):
    movie_name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.now)

    # This returns the object name by default. Instead we set it to movie name for admin view!
    def __str__(self):
        return self.movie_name

from django.db import models
from django.contrib.auth.models import User


class Disc(models.Model):
    Title = models.CharField(max_length=120)
    Artist = models.CharField(max_length=120)
    Release_Year = models.IntegerField()
    Format = models.CharField(max_length=120)

    class Meta:
        db_table = 'Disc'

    def __str__(self):
        return self.Title


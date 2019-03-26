from django.db import models

# Create your models here.

class Paths(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introdution = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)


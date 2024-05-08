from django.db import models

# Create your models here.
from django.db import models

class Report(models.Model):
    National_ID = models.CharField(max_length=14, default=None)
    Name = models.CharField(max_length=200, default=None)
    Complaints = models.TextField()


    def __str__(self):
      return f"{self.National_ID}"

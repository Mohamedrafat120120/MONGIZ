from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class educational_state (models.Model):
    id_number = models.CharField(max_length=14, default=None)
    name = models.CharField(max_length=200, default=None)
    Schools = models.CharField(max_length=200, default=None)
    University = models.CharField(max_length=200, default=None)

def __str__(self):
    return f"{self.name}"

class certification(models.Model):
    Degree = models.CharField(max_length=100 , default=None)
    certification = models.ImageField(null=True)  ##don't forget to create an image file


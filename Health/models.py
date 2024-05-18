from django.db import models
from account.models import User


class Blood_type(models.TextChoices):
    A_PLUS = "A+",
    A_MINUS = "A-",
    B_PLUS = "B+",
    B_MINUS = "B-",
    AB_PLUS = "AB+",
    AB_MINUS = "AB-",  
    O_PLUS = "O+" , 
    O_MINUS = "O-",


class health_state (models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    Name = models.CharField(max_length=200, default=None)
    Blood_Quarter = models.CharField(max_length=3, choices=Blood_type.choices, default=None)
    Health_Problem = models.CharField(max_length=500, default=None)

    def __str__(self):
      return self.Name


class medical_history (models.Model):
    Chronic_Diseases = models.CharField(max_length=100,default=None)
    Another_Diseases = models.CharField(max_length=100, default=None)



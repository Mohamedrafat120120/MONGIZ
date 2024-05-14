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
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    id_number = models.CharField(max_length=15, default=None,primary_key=True)
    name = models.CharField(max_length=200, default=None)
    Blood_quarter = models.CharField(max_length=3, choices=Blood_type.choices, default=None)
    health_problem = models.CharField(max_length=500, default=None)

    def __str__(self):
      return self.name


class medical_history (models.Model):
    chronic_diseases = models.CharField(max_length=100,default=None)
    another_diseases = models.CharField(max_length=100, default=None)



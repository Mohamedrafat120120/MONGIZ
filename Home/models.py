from django.db import models
from Health.models import health_state
from account.models import User

class MaritalState(models.TextChoices):
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'

class Blood_type(models.TextChoices):
    A_PLUS = "A+",
    A_MINUS = "A-",
    B_PLUS = "B+",
    B_MINUS = "B-",
    AB_PLUS = "AB+",
    AB_MINUS = "AB-",  
    O_PLUS = "O+" , 
    O_MINUS = "O-",

class Home_page(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    Id_Num=models.CharField(max_length=15,default=None,null=False,blank=False,primary_key=True)
    Name = models.CharField(max_length=200, default=None)
    Nationality = models.CharField(max_length=100, default=None)
    Marital_state = models.CharField(max_length=9, choices=MaritalState.choices, default=MaritalState.SINGLE)
    Blood_quarter = models.CharField(max_length=3,choices=Blood_type.choices ,default=None)
    Address = models.CharField(max_length=40, default=None)
    BirthDate = models.DateField()

    def __str__(self):
      return self.Name



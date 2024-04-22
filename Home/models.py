from django.db import models
from Health.models import health_state
from account.models import User

class MaritalState(models.TextChoices):
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'

class Blood_type(models.TextChoices):
    A = 'A+'
    a = 'A-'
    B = 'B'
    AB = 'AB'
    O = 'O'

class Home_page(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user",null=True)
    Name = models.CharField(max_length=200, default=None)
    Nationality = models.CharField(max_length=100, default=None)
    Marital_state = models.CharField(max_length=9, choices=MaritalState.choices, default=MaritalState.SINGLE)
    Blood_quarter = models.CharField(max_length=3,choices=Blood_type.choices ,default=None)
    Address = models.CharField(max_length=40, default=None)
    BirthDate = models.DateField()

    def __str__(self):
      return self.Name



from django.db import models
from account.models import User

class MaritalState(models.TextChoices):
    SINGLE ='Single'
    MARRIED =  'Married'
    DIVORCED =  'Divorced'
    WIDOWED =  'Widowed'

class social_state(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    Name = models.CharField(max_length=200, default=None)
    Personel_Card = models.ImageField()
    Marital_state = models.CharField(max_length= 9, choices=MaritalState.choices, default=MaritalState.SINGLE)
    Phone_Number = models.CharField(max_length=14, default=None)
    Address = models.CharField(max_length=40,default=None)

    def __str__(self):
      return self.Name

class Family(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    Name = models.CharField(max_length=200, default=None)
    husband_or_wife = models.CharField(max_length=200, default=None)
    Sons_number = models.IntegerField()
    sons_name = models.CharField(max_length=100, default=None)


    def __str__(self):
      return self.Name





from django.db import models
from account.models import User

# Create your models here.
from django.db import models

class Report(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    National_ID = models.CharField(max_length=14, default=None,null=False,blank=False,primary_key=True)
    Name = models.CharField(max_length=200, default=None)
    Complaints = models.TextField()


    def __str__(self):
      return f"{self.National_ID}"

from django.db import models
from account.models import User

# Create your models here.
from django.db import models

class Report(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.PROTECT)
    ID=models.CharField(max_length=15,blank=False,null=False)
    Name = models.CharField(max_length=200, default='',null=False,blank=False)
    Complaints = models.TextField()


    def national_id(self):
      return f"{self.Sender.national_id}"

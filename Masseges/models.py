from django.db import models

# Create your models here.
class masseges(models.Model):
    Issue=models.TextField(max_length=255,null=False,blank=False,default='Write your issue')
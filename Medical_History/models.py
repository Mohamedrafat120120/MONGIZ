from django.db import models
from account.models import User
# Create your models here.


class medical_history(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Name = models.CharField(max_length=200, default=None,null=False,blank=False)
    Age=models.IntegerField(null=False,blank=False)
    Chronic_Diseases = models.TextField(max_length=100,default=None)
    Another_Diseases = models.TextField(max_length=100, default=None)
    def national_id(self):
        National_Id=f"{self.User.national_id}"
        return  National_Id
from django.db import models
from datetime import datetime
from account.models import User

# Create your models here.
class nationality(models.TextChoices):
    Egyptian="Egyptian"
    
class blood(models.TextChoices):
    A_PLUS = "A+",
    A_MINUS = "A-",
    B_PLUS = "B+",
    B_MINUS = "B-",
    AB_PLUS = "AB+",
    AB_MINUS = "AB-",  
    O_PLUS = "O+" , 
    O_MINUS = "O-",
    
def get_first_day_next_month():
    today = datetime.date.today()
    next_month = today.replace(day=1, month=today.month % 12 + 1, year=today.year + (today.month // 12))
    return next_month    
    
class Personal_ID_Card(models.Model):
    Sender=models.ForeignKey(User,related_name='sender_reniew_id',on_delete=models.CASCADE,default=None)
    Full_Name=models.CharField(max_length=255,default=None,blank=False,null=False)
    Birth_dt=models.DateField(blank=False,null=False)
    Full_Address=models.CharField(max_length=255,default=None)
    National_ID=models.CharField(max_length=15,default=None,blank=False,null=False)
    Current_Job=models.CharField(max_length=255,default=None,blank=False,null=False)
    Marital_State=models.CharField(max_length=255,default=None,blank=False,null=False)
    Study_Field=models.CharField(max_length=255,default=None,blank=False,null=False)
    Recent_Personal_Image=models.ImageField(upload_to='Reniew_ID_Photo/%y/%m/%d')
    Request_Date=models.DateField(auto_now=True)
    Receive_Date=models.DateField()
    def __int__(self):
        return self.pk
class Personal_Driving_License(models.Model):
    Sender=models.ForeignKey(User,related_name='sender_driving_license',on_delete=models.CASCADE,default=None)
    Name_in_Arabic=models.CharField(max_length=255,default=None,blank=False,null=False)
    Name_in_English=models.CharField(max_length=255,blank=False,null=False)
    Full_Address=models.CharField(max_length=255,default=None)
    National_ID=models.CharField(max_length=15,default=None,blank=False,null=False)
    Job=models.CharField(max_length=255,default=None,blank=False,null=False)
    Marital_State=models.CharField(max_length=255,default=None,blank=False,null=False)
    Nationality=models.CharField(max_length=255,choices=nationality.choices,blank=False,null=False)
    Traffic_Department=models.CharField(max_length=255,default=None,blank=False,null=False)
    Blood_Type=models.CharField(max_length=13,choices=blood.choices,blank=False,null=False)
    Medical_Examine_Image=models.ImageField(upload_to='Reniew_Driving_License_Photo/Medical_Examine/%y/%m/%d')
    Request_Date=models.DateField(auto_now=True)
    Receive_Date=models.DateField()
    
    def __int__(self):
        return self.pk
    
    
    
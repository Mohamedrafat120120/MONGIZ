from django.db import models
from datetime import date
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
  

def recieve_date(date_now):
  date_now= date.today()
  if date_now.month == 12:
    y = str(date_now.year+1) + '-' + str(date_now.month+1) + '-' + str(date_now.day)
    return y  
  else:
    y =str(date_now.year) + '-' + str(date_now.month+1) + '-' + str(date_now.day) 
    return  y      
    
class Personal_ID_Card(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.PROTECT)
    Full_Name=models.CharField(max_length=255,blank=False,null=False)
    Birth_dt=models.DateField(blank=False,null=False)
    Full_Address=models.CharField(max_length=255,default=None)
    National_ID=models.CharField(max_length=15,default=None,blank=False,null=False)
    Current_Job=models.CharField(max_length=255,default=None,blank=False,null=False)
    Marital_State=models.CharField(max_length=255,default=None,blank=False,null=False)
    Study_Field=models.CharField(max_length=255,default=None,blank=False,null=False)
    Recent_Personal_Image=models.ImageField(upload_to='Reniew_ID_Photo/%y/%m/%d')
    Request_Date=models.DateField(auto_now_add=True)
    Receive_Date=models.DateField(default=recieve_date(Request_Date))
    def __str__(self):
        return self.Sender.national_id
  
class Personal_Driving_License(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.PROTECT)
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
    Receive_Date=models.DateField(default=recieve_date(Request_Date))
    
    def __str__(self):
        return self.Sender.national_id
    
    
    
from django.db import models
from  account.models import User
# Create your models here.

class Skills(models.TextChoices):
    Html="Html"
    Css="Css"
    Javascript= "Javascript"
    React= "React"
    Angular="Angular"
    Vue = 'Vue.js'
    Photoshop='Photoshop'
    Illustrator= "Illustrator"
    Python= "Python"
    Flask= "Flask"
    Django="Django"
    Nodejs= "Node.js"
    C="C#"
    MongoDB= "MongoDB"
    SQl= "SQL"
    PostgressSQL= "PostgreSQL"
    Git= "Git"
    Github= "Github"
    Power_BI= "Power BI"
    UIUX= "UI/UX Designing"
    Figma= "Figma"
    Xd= "Adobe XD"
    Excel= "Microsoft Excel" 
    Word= "Microsoft Word"  
    PowerPoint= "Microsoft Power Point"
    Content_Creator= "Content Creator"
    Writing= "Writing"
    Translation= "Translation"
    Editing= "Editing"
    Video_Editing= "Video Editing"
    Pr="Adobe Pr"
    
    
class Personal_Info(models.Model):
    Full_Name=models.CharField(max_length=100,default=" ",null=False,blank=False)
    Email=models.EmailField(unique=True,default=" ")
    Profession=models.CharField(max_length=100,default=" ",null=False,blank=False)
    Address=models.CharField(max_length=100,default=" ",null=False,blank=False)
    City=models.CharField(max_length=100,default=" ",null=False,blank=False)
    state=models.CharField(max_length=100,default="Egypt",null=False,blank=False)
    def __str__(self) -> str:
        return self.Email
    
    
class Expereince(models.Model):
       company=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Employer=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Role=models.CharField(max_length=100,default=" ",null=False,blank=False)
       company_Address=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Start_Date=models.DateField(default=" ",null=False,blank=False)
       Finish_Date=models.DateField(default=" ",null=False,blank=False)
       Currently_work_here=models.BooleanField(default=False)
       
       
        
class Education(models.Model):
    School_Name=models.CharField(max_length=100,default=" ",null=False,blank=False)
    School_Location=models.CharField(max_length=100,default=" ",null=False,blank=False) 
    Degree_Program=models.CharField(max_length=100,default=" ",null=False,blank=False)      
    Field_Of_Study=models.CharField(max_length=100,default=" ",null=False,blank=False)      
    Graduation_Month_and_Year=models.DateField(default=" ",null=False,blank=False)
      
          
class Technical_Skill(models.Model):        
     Skill1=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill2=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill3=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill4=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill5=models.CharField(max_length=50,choices=Skills.choices,unique=True)
class Contact_Info(models.Model):
      Phone_Number=models.CharField(max_length=11,default=" ")   
      Linkedin_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False)    
      Twitter_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False)    
      GitHub_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False)    
      Portfolio_Link=models.URLField(max_length=100,default="https/",null=False,blank=False) 


         
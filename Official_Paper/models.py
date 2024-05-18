from django.db import models
from Social.models import social_state
from account.models import User
class papers(models.Model):
    ID_number = User.national_id
    Name = social_state.Name
    Bith_cirtification = models.ImageField()
    ID_card = social_state.Personel_Card
    Passport = models.ImageField(upload_to='Passport_Photo/%y/%m/%d')
    Driving_Licence = models.ImageField()

    def __str__(self):
     return f"{self.Name}"
    
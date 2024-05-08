from django.db import models

class work_career(models.Model):
    Current_Jop = models.CharField(max_length=200, default=None)
    Campanies = models.TextField()
    Other = models.TextField(default=None)

    # def __int__(self):
    #   return self.pk
    
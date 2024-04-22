from django.db import models

class work_career(models.Model):
    ID_number = models.CharField(max_length=14, default=None)
    Name = models.CharField(max_length=200, default=None)
    current_jop = models.CharField(max_length=200, default=None)
    campanies = models.TextField()
    other = models.TextField()

    def __str__(self):
      return f"{self.Name}"
    
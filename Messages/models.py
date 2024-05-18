from django.db import models
from account.models import User

class message(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    Header = models.CharField(max_length=20, default=None)
    Content = models.TextField(max_length=300, default=None)

    def __str__(self):
        return self.Header

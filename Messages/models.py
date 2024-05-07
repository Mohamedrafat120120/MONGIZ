from django.db import models


class message(models.Model):
    Header = models.CharField(max_length=20, default=None)
    content = models.TextField(max_length=300, default=None)

    def __int__(self):
        return self.pk

from django.contrib.auth.models import User
from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True)

    def __str__(self):
        return self.name


# Create your models here.

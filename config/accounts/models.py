from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username
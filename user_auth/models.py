from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name

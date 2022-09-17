from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=30)

    def _str_(self):
       return self.name
from django.db import models

# Create your models here.
class Blogsite(models.Model):
    name=models.CharField(max_length=100)
    description= models.TextField(max_length=50)
    def __str_(self):
        return 
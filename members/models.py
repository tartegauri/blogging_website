from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(null=True,max_length=25)
    age = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    password = models.CharField(null=True,max_length=25)
    phone = models.IntegerField(null=True)

class Blogs(models.Model):
    heading = models.CharField(null=True,max_length=50)
    content = models.CharField(null=True,max_length=255)
    byid = models.IntegerField(null=False)
    byuser = models.CharField(null=True,max_length=50) 
from django.db import models

# Create your models here.
class Table20(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Country=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Image(models.Model):
    Name=models.CharField(max_length=20)
    Brand=models.CharField(max_length=20)
    Price=models.IntegerField()
    Model=models.CharField(max_length=40)
    Engine=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
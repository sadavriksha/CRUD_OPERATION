from django.db import models


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    Username = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    Email = models.CharField(max_length=100)
    Password= models.CharField(max_length=100)
    Confirm=models.CharField(max_length=100)
    Address= models.ForeignKey(Position,on_delete=models.CASCADE)

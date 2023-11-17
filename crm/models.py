from django.db import models

# Create your models here.

class Employees(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveBigIntegerField()
    contacts=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)

#to replace employee object (1) as objects by its name
    def __str__(self):
        return self.name
    
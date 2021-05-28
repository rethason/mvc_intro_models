
#from typing_extensions import ParamSpec
from django.db import models
from datetime import datetime

# Create your models here.
class School(models.Model):
    name =models.CharField(max_length=400)

class Faculty(models.Model):
    name =models.CharField(max_length=400)

class Department(models.Model):
    Faculty =models.ForeignKey(Faculty,on_delete=models.CASCADE)
    name =models.CharField(max_length=400)

class Certificate_type (models.Model):
    name =models.CharField(max_length=400)

class Grade(models.Model):
    type =models.CharField(max_length=100)

class Student(models.Model):
    School =models.ForeignKey(School,on_delete=models.CASCADE)
    Department =models.ForeignKey(Department,on_delete=models.CASCADE)
    Certificate_type =models.ForeignKey(Certificate_type,on_delete=models.CASCADE)
    Grade =models.ForeignKey(Grade,on_delete=models.CASCADE)
    fullname =models.CharField(max_length=400)
    year =models.PositiveBigIntegerField()


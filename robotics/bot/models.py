from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    fees_paid = models.BooleanField(default=False)

options = [("owner","Owner"),("manager","Manager")]
class Employee(models.Model):
    role = models.CharField(max_length=20 , choices=options , default="employee")
    name = models.CharField(max_length=20)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    username = models.CharField(max_length=20 , unique=True)
    password = models.CharField(max_length=20)
    dob = models.DateField()
    terms = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="profiles/", default="/profiles/default.png")
    
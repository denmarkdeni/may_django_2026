from django.db import models
from django.contrib.auth.models import User

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
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    options = [
        ("vegetables","Vegetables"),
        ("fruits", "Fruits"),
        ("groceries", "Groceries"),
        ("medicines" , "Medicines")
    ]
    category = models.CharField(max_length=20, choices=options)
    expiry_date = models.DateField()

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    options = [
        ("admin","Admin"),
        ("staff","Staff"),
        ("customer","Customer")
    ]
    role = models.CharField(max_length=20, choices=options)
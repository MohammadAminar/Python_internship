from abc import ABC, abstractmethod
from django.db import models

class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Phone = models.IntegerField(max_length=50)
    International_code = models.IntegerField(max_length=50)

class Teacher(User, models.Model):
    CHOICES = [
        ('True', 'بله'),
        ('False', 'خیر'),
    ],
    User_Id = models.AutoField(primary_key=True)
    Code_vezarat_olom = models.IntegerField(max_length=50)
    Work_experience = models.BooleanField(default=False, choices=CHOICES)
    Education = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Student(User, models.Model):
    DEBT_STATUS_CHOICES = [
        ('SUSPENDED', 'معلق شده'),
        ('PAID', 'پرداخت شده'),
        ('UNPAID', 'پرداخت نشده'),
    ],
    User_Id = models.AutoField(primary_key=True)
    Education_level = models.CharField(max_length=50)
    Debt_status = models.CharField(max_length=50, choices=DEBT_STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Parent(User, models.Model):
    User_Id = models.AutoField(primary_key=True)
    Number_of_children = models.IntegerField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Manager(User, models.Model):
    User_Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

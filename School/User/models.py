from abc import ABC, abstractmethod
from django.db import models

class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    International_code = models.CharField(max_length=50)

class Teacher(User, models.Model):
    User_Id = models.AutoField(primary_key=True)
    Code_vezarat_olom = models.CharField(max_length=50)
    Work_experience = models.BooleanField(default=False)
    Education = models.CharField(max_length=50)

class Student(User):
    User_Id = models.AutoField(primary_key=True)
    Education_level = models.CharField(max_length=50)
    Debt_status = models.CharField(max_length=50)

class Parent(User):
    User_Id = models.AutoField(primary_key=True)
    Number_of_children = models.CharField(max_length=50)

class Manager(User):
    User_Id = models.AutoField(primary_key=True)

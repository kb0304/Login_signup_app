from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.storage import FileSystemStorage

class User(models.Model):
    name = models.CharField(max_length=70)
    enrollment_no = models.IntegerField()
    
    #MaxValueValidator(99999999),MinValueValidator(9999999))
    
    about_me = models.CharField(max_length=5000)
    profile_pic = models.ImageField(upload_to = '/ag53/images/profile_pic/')
    cover_pic = models.ImageField(upload_to = '/ag53/images/cover_pic/')

class Email(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField(max_length = 254)

class Password(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(max_length = 30)

class Gender(models.Model):
    gender = models.CharField(max_length = 1)
    user = models.ManyToManyField(User)

class Branch(models.Model):
    branch = models.CharField(max_length = 100)
    user = models.ManyToManyField(User)

class Age(models.Model):
    user = models.ManyToManyField(User)
    age = models.IntegerField()
    
    #MaxValueValidator(150),MinValueValidator(0))



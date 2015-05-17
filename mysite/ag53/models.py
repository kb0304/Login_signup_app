from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_delete
import os

#################################################################################################

class Gender(models.Model):
    gender = models.CharField(max_length = 1,default = 'd')
    def __unicode__(self):
        return self.gender
#################################################################################################

class Branch(models.Model):
    branch = models.CharField(max_length = 100, default = 'default_value')
    def __unicode__(self):
        return self.branch

###############################################################################################

class Age(models.Model):
    age = models.IntegerField(default=1)
    #MaxValueValidator(150),MinValueValidator(0))
    def __unicode__(self):
        return "%s"%(self.age,)
################################################################################################

def rename_and_upload_profile_pic(instance,filename):
    path = 'ag53/images/profile_pic/'
    ext = filename.split('.')[-1]
    enrollment_no = instance.enrollment_no
    filename = '{}'.format(enrollment_no,ext)
    return os.path.join(path, filename)


def rename_and_upload_cover_pic(instance,filename):
    path = 'ag53/images/cover_pic/'
    ext = filename.split('.')[-1]
    enrollment_no = instance.enrollment_no
    filename = '{}'.format(enrollment_no,ext)
    return os.path.join(path, filename)



class User(models.Model):
    name = models.CharField(max_length=70, default = 'default_value')
    enrollment_no = models.IntegerField(default = 0)
    
    #MaxValueValidator(99999999),MinValueValidator(9999999))
    
    about_me = models.CharField(max_length=5000, default = 'default_value')
    profile_pic = models.ImageField(upload_to = rename_and_upload_profile_pic)
    cover_pic = models.ImageField(upload_to = rename_and_upload_cover_pic)
    age = models.ForeignKey(Age, default=1)
    branch = models.ForeignKey(Branch, default=1)
    gender = models.ForeignKey(Gender, default=1)
    def __unicode__(self):
        return self.name+"_%s"%(self.enrollment_no,)

def delete_profile_and_cover_pics(sender, **kwargs):
    user = kwargs.get('instance')
    try:
        os.remove(user.profile_pic.path)
        os.remove(user.cover_pic.path)
    except:
        pass
post_delete.connect(delete_profile_and_cover_pics, User)


#################################################################################################

class Email(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField(max_length = 254)

#################################################################################################

class Password(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(max_length = 30, default = 'default_value')

#################################################################################################



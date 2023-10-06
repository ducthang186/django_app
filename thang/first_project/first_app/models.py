from django.db import models
# from django.contrib.auth.models import User

from .forms import FormName
# Create your models here.
# class User(models.Model):
#     FirstName = models.CharField(max_length=200)
#     LastName = models.CharField(max_length=200)
#     Email = models.EmailField(max_length=200)

    
class User1(models.Model):
    firstname =  models.CharField(max_length=264)
    lastname =  models.CharField(max_length=264)
    email =  models.CharField(max_length=264)

    def __str__(self):
        return self.firstname


class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,)
    name = models.CharField(max_length=264)
    url = models.URLField()
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE,)
    date = models.DateField()
   
    def __str__(self):
         return self.date

class MyForm(models.Model):
    name = models.CharField(max_length=255)
    email  = models.EmailField()
    text = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    



# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     # additional
#     portfolio_site = models.URLField(blank=True)

#     profile_pic = models.ImageField(upload_to="profile_pic",blank=True)

#     def __str__(self):
#         return self.user.username
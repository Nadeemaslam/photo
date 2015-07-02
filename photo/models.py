from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(max_length=200,blank=True)
    image = models.ImageField(upload_to="images/",null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.image.name





from django.contrib.auth.models import User


# class UserProfile(models.Model):
#         # This field is required.
#         user = models.OneToOneField(User)
#         # These fields are optional
#         website = models.URLField(blank=True)
        

#         def __unicode__(self):
#                 return self.user.username


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





# from string import join

# import os
# from PIL import Image as PImage
# from albumsite.settings import MEDIA_ROOT

# class Image(models.Model):
#     # ...

#     def save(self, *args, **kwargs):
#         """Save image dimensions."""
#         super(Image, self).save(*args, **kwargs)
#         im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
#         self.width, self.height = im.size
#         super(Image, self).save(*args, ** kwargs)

#     def size(self):
#         """Image size."""
#         return "%s x %s" % (self.width, self.height)

#     def __unicode__(self):
#         return self.image.name

#     def tags_(self):
#         lst = [x[1] for x in self.tags.values_list()]
#         return str(join(lst, ', '))

#     def albums_(self):
#         lst = [x[1] for x in self.albums.values_list()]
#         return str(join(lst, ', '))

#     def thumbnail(self):
#         return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
#                                                                     (self.image.name, self.image.name))
#     thumbnail.allow_tags = True


# class ImageAdmin(admin.ModelAdmin):
#     # search_fields = ["title"]
#     list_display = ["__unicode__", "title", "user", "rating", "size", "tags_", "albums_",
#         "thumbnail", "created"]
#     list_filter = ["tags", "albums", "user"]

#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()


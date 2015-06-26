from django.contrib import admin
from photo.models import Album,Image,Tag


admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Image)

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from photo.models import Image
class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]

# class UserProfileForm(forms.ModelForm):
#         class Meta:
#                 model = UserProfile
#                 fields = ["user", "website"]

class AddImage(ModelForm):
	class Meta:
		model = Image
		fields =["title","description","image","albums"]

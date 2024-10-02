from django import forms
from django.forms import ModelForm
from .models import profile

class AddCoverImage(ModelForm):
    class Meta:
        model = profile
        fields = ('cover_image',)
        labels = {
            'cover_image': '',
        }


class AddProfileImage(ModelForm):
    class Meta:
        model = profile
        fields = ('profile_image',)
        labels = {
            'profile_image': '',
        }
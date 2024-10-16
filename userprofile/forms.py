from django import forms
from django.forms import ModelForm
from .models import Profile

class AddCoverImage(ModelForm):
    class Meta:
        model = Profile
        fields = ('cover_image',)
        labels = {
            'cover_image': '',
        }


class AddProfileImage(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)
        labels = {
            'profile_image': '',
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'cover_image',
            'profile_image',
            'title',
            'social_links',
        ]
        labels = {
            'bio': 'About',
            'cover_image': 'Cover Image',
            'profile_image': 'Profile Image',
            'title': 'Title',
            'social_links': 'Social Links',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-textarea'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'social_links': forms.Textarea(attrs={'class': 'form-textarea'}),
        }

class AddBio(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
        labels = {
            'bio': 'About',
        }
from django import forms
from django.forms import ModelForm
from .models import Profile
from authentication.models import Student

class AddCoverImage(ModelForm):
    class Meta:
        model = Profile
        fields = ['cover_image']
        labels = {
            'cover_image': 'Cover Image',
        }
        widgets = {
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'id_cover_image',
                'accept': 'image/*'
            })
        }


class AddProfileImage(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
        labels = {
            'profile_image': 'Profile Image',
        }
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'id_profile_image',
                'accept': 'image/*'
            })
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
            'bio': forms.Textarea(attrs={
                'class': 'rounded-lg border border-gray-300 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 w-[500px] h-[150px]',
                'style': 'resize:none'
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'id_cover_image',
                'accept': 'image/*'
            }),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'id_profile_image',
                'accept': 'image/*'
            }),
            'title': forms.TextInput(attrs={
                'class': 'rounded-lg border border-gray-300 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500',
                'style': 'overflow: auto; width: 500px;'
            }),
            'social_links': forms.HiddenInput(),
        }


class AddBio(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        labels = {
            'bio': 'About',
        }
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'flex text-[11px] rounded-lg border border-gray-300 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 w-full overflow-x-hidden overflow-y-auto no-scrollbar',
                'rows': 6,
                'style': 'resize:none'
            }),
        }

class AddLinks(ModelForm):
    class Meta:
        model = Profile
        fields = ['social_links']
        labels = {
            'social_links': 'Links',
        }
        widgets = {
            'social_links': forms.HiddenInput(),
        }

    
class VerifyAccount(ModelForm):
    class Meta:
            model = Student
            fields = ['email','password']



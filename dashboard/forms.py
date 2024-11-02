from django import forms
from .models import Post, Comment, Report

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image'] # images implemented
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'w-full focus:outline-none rounded-lg border-none font-normal text-gray-font2 bg-gray-box text-sm placeholder-gray-font',
                'placeholder': 'What\'s on your mind?'
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'id_image',
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report 
        fields = ['reason', 'reason_category']
        widgets = {
            'reason': forms.Textarea(attrs={
                'placeholder': 'Please provide a reason for reporting this post'
            }),
            'reason_category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
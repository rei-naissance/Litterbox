from django import forms
from .models import Post, Comment, Report, Announcement

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'placeholder-gray-font w-full focus:outline-none rounded-lg border border-border-gray font-normal text-gray-font2 text-sm placeholder-gray-font',
                'placeholder': 'Enter title here...',
            }),
            'content': forms.Textarea(attrs={
                'class': 'placeholder-gray-font w-full h-80 rounded-lg text-sm font-normal text-black border border-border-gray hover:bg-bg-gray',
                'placeholder': 'Write your post here...',
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'id_image',
                'class': 'block w-full text-sm text-gray-500 border border-border-gray rounded-lg cursor-pointer bg-bg-gray hover:bg-bg-hover-gray focus:outline-none',
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
                'placeholder': 'Please provide a reason for reporting this post',
                'class': 'placeholder-gray-font w-full h-80 rounded-lg text-sm font-normal text-black border border-border-gray hover:bg-bg-gray'
            }),
            'reason_category': forms.Select(attrs={
                'class': 'w-full h-9 rounded-lg text-sm font-normal text-black border border-border-gray hover:bg-bg-gray'
            }),
        }

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'is_archived']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter announcement details',
                'rows': 5
            }),
            'is_archived': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }
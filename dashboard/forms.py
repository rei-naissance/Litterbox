from django import forms
from .models import Post, Comment, Report

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image'] # add image to fields when ready to implement
        widgets = {
            'content': forms.TextInput(attrs={'class': 'w-full focus:outline-none rounded-lg border border-border-gray font-normal text-gray-font2 text-sm placeholder-gray-font', 'placeholder': 'Enter title here...'}),
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
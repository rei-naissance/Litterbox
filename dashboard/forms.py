from django import forms
from .models import Post, Comment, Report, Announcement
from .models import Post, Comment, Report, Event
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'placeholder-gray-font w-full focus:outline-none rounded-lg border border-border-gray font-normal text-gray-font2 text-sm placeholder-gray-font',
                'placeholder': 'Enter title here...',
            }),
            'content': TinyMCE(attrs={
                'class': 'placeholder-gray-font w-full h-96 rounded-lg text-sm font-normal text-black border border-border-gray hover:bg-bg-gray',
                'placeholder': 'Write your post here...',  # TinyMCE doesn't use this, but keeping it won't hurt
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
            'content': TinyMCE(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter announcement details',
                'rows': 5
            }),
            'is_archived': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 
                  'start_date', 
                  'start_time', 
                  'end_date', 
                  'end_time', 
                  'location', 
                  'description',
                  'image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),  
            'end_time': forms.TimeInput(attrs={'type': 'time'}),  
            'location': forms.TextInput(attrs={'placeholder': 'Enter location here...'}), 
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter event description...'}),
        }
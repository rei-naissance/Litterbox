from django import forms
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Student
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        
        # Add Tailwind CSS classes to form fields
        self.fields['email'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Enter your email',
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Choose a password',
        })
        
        self.fields['confirm_password'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Confirm your password',
        })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match.')

class StudentLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    
    def __init__(self, *args, **kwargs):
        super(StudentLoginForm, self).__init__(*args, **kwargs)
        
        # Add Tailwind CSS classes to form fields
        self.fields['username'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Enter your email',
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Enter password',
        })

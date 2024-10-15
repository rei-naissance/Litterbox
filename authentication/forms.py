from django import forms
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Student
        fields = ['email', 'password']

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
            'placeholder': 'Enter your username',
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'w-full border-input-border rounded-sm py-2 px-4 focus:border-gray-500',
            'placeholder': 'Enter password',
        })

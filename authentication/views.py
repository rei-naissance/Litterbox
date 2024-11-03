from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from .models import Student
from .forms import StudentRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_user = Student.objects.filter(email=email).first()

            if existing_user:
                if not existing_user.is_active:
                    messages.info(request, 'An unverified account with this email already exists.')
                else:
                    messages.info(request, 'An account with this email already exists. Please log in.')
                return redirect('register')
                
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.is_verified = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Litterbox Account'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'philippeandrei.dael@cit.edu', [user.email])

            return redirect('activation_sent', user_id=user.id)
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})

def resend_verification_email(request, user_id):
    user = Student.objects.filter(pk=user_id).first()

    if user and not user.is_verified:
        current_site = get_current_site(request)
        subject = 'Resend: Activate Your Litterbox Account'
        message = render_to_string('activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(subject, message, 'philippeandrei.dael@cit.edu', [user.email])
        messages.info(request, 'A new verification email has been sent. Please check your Outlook inbox.')
    else:
        messages.error(request, 'This account is already verified or does not exist.')

    return redirect('activation_sent', user_id=user.id)


def activate_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Student.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Student.DoesNotExist):
        user = None

    # Debugging line, was used to check if emails were actually being sent
    print(f"UID: {uid}, Token: {token}, User Exists: {user is not None}")
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.save()
        login(request, user)
        return redirect('dashboard_home')
    else:
        return render(request, 'activation_failed.html')

def login_view(request):
    pass
    
def activation_sent(request, user_id):
    return render(request, 'activation_sent.html', {'user_id': user_id})

def index(request):
    return render(request, 'home.html')


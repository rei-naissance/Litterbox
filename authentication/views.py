from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
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
            existing_user = Student.objects.filter(email=email).first() # Boolean to check if the account is existing in the database.

            # Checker for existing accounts using existing_user boolean.
            if existing_user:
                if not existing_user.is_active:
                    messages.info(request, 'An unverified account with this email already exists.')
                else:
                    messages.info(request, 'An account with this email already exists. Please log in.')
                return redirect('register')
            
            # Temporarily save details while waiting for verification.
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.is_verified = False
            user.save()

            # Email construction.
            current_site = get_current_site(request)                                            # Used to later retrieve url domain.
            subject = 'Activate Your Litterbox Account'                                         # Email subject.
            message = render_to_string('activation_email.html', {                               # Email body utilizing template.
                'user': user,                                                                   # Email owned by user.
                'domain': current_site.domain,                                                  # Domain of site.
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),                             # Encoded user id.
                'token': default_token_generator.make_token(user),                              # Token generated for user.
            })
            send_mail(subject, message, 'elwison.denampo@cit.edu', [user.email])            # SMTP function to send mail.

            return redirect('activation_sent', user_id=user.id) 
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})

def resend_verification_email(request, user_id):
    user = Student.objects.filter(pk=user_id).first()

    if user and not user.is_verified:
        # Email construction (same as aforementioned code in registration).
        current_site = get_current_site(request)
        subject = 'Resend: Activate Your Litterbox Account'
        message = render_to_string('activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(subject, message, 'elwison.denampo@cit.edu', [user.email])

    # Debugging lines
    """
        messages.info(request, 'A new verification email has been sent. Please check your Outlook inbox.')
    else: 
        messages.error(request, 'This account is already verified or does not exist.')
    """
    return redirect('activation_sent', user_id=user.id)


def activate_view(request, uidb64, token):
    # Decode the uid passed through the email and token from the URL.
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Student.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Student.DoesNotExist):
        user = None

    # Debugging line, was used to check if emails were actually being sent.
    # print(f"UID: {uid}, Token: {token}, User Exists: {user is not None}")
    
    # Check if the user exists and the token is valid.
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.save()
        login(request, user)
        return redirect('dashboard_home')
    else:
        return render(request, 'activation_failed.html')
    
def activation_sent(request, user_id):
    return render(request, 'activation_sent.html', {'user_id': user_id})

def index(request):
    return render(request, 'home.html')

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Student.objects.filter(email=email).first()
        if user:
            subject = 'Password Reset'
            current_site = get_current_site(request)
            message = render_to_string('password_reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'elwison.denampo@cit.edu', [user.email])
            messages.success(request, 'Password reset email sent.')
            return redirect('password_reset_sent')
        else:
            messages.error('Account with this cit.edu email does not exist.')
    return render(request, 'password_reset_form.html')

def password_reset_confirmation(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Student.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Student.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password successfully changed.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match. Please try again.')
                return render(request, "password_reset_confirm.html", {'user': user})
        else:
            return render(request, "password_reset_confirm.html", {'user': user})
    else:
        messages.error(request, 'This link is invalid or has expired.')
        return redirect('password_reset')
    
def password_reset_sent(request):
    return render(request, 'password_reset_sent.html')  
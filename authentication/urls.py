from django.urls import path
from .views import register_view, activate_view, activation_sent, resend_verification_email, index
from django.contrib.auth.views import LoginView
from .forms import StudentLoginForm

urlpatterns = [
    path('', register_view, name='register'),
    path('register/', register_view, name='register'),
    path('activate/<uidb64>/<token>/', activate_view, name='activate'),
    path('activation_sent/<int:user_id>/', activation_sent, name='activation_sent'),
    path('resend-verification/<int:user_id>/', resend_verification_email, name='resend_verification_email'),
    path('index/', index, name='index'),
    path('login/', LoginView.as_view(
        template_name = 'login.html',
        authentication_form = StudentLoginForm,
        ), name='login')
]
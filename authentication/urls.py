from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .forms import StudentLoginForm

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_view, name='register'),
    path('activate/<uidb64>/<token>/', views.activate_view, name='activate'),
    path('activation_sent/<int:user_id>/', views.activation_sent, name='activation_sent'),
    path('resend-verification/<int:user_id>/', views.resend_verification_email, name='resend_verification_email'),
    path('index/', views.index, name='index'),
    path('login/', LoginView.as_view(
        template_name = 'login.html',
        authentication_form = StudentLoginForm,
        ), name='login'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/sent/', views.password_reset_sent, name='password_reset_sent'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirmation, name='password_reset_confirmation'),
    path('logout/', views.logout, name='logout'),
]
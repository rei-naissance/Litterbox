from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('account_termination/', views.account_termination, name='account_termination'),
]

urlpatterns += staticfiles_urlpatterns()
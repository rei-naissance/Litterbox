from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
]

urlpatterns += staticfiles_urlpatterns()
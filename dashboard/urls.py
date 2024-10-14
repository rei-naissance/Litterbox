from django.urls import path
from django.conf.urls.static import static

from Litterbox import settings
from . import views

urlpatterns = [
    path('dashboard_home/', views.dashboard_home, name='dashboard_home'),
]


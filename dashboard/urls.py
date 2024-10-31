from django.urls import path
from django.conf.urls.static import static

from Litterbox import settings
from . import views

urlpatterns = [
    path('dashboard_home', views.dashboard_home, name='dashboard_home'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('post/<int:post_id>/send_report', views.send_report, name='send_report'),
    path('report/<int:report_id>/delete/', views.delete_reported_post, name='delete_reported_post'),
    path('report/<int:report_id>/ignore/', views.disregard_reported_post, name='disregard_reported_post'),
    path('toggle-like/<int:post_id>/', views.toggle_like, name='toggle_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
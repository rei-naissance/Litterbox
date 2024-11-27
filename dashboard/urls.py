from django.urls import path
from django.conf.urls.static import static

from Litterbox import settings
from . import views

urlpatterns = [
    path('dashboard_home/', views.dashboard_home, name='dashboard_home'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('post/<int:post_id>/send_report', views.send_report, name='send_report'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path('event/save/', views.save_event, name='save_event'),
    path('events/', views.get_events, name='get_events'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('events/user/', views.user_events, name='user_events'),
    path('follow-event/<int:event_id>/', views.follow_event, name='follow_event'),
    path('unfollow-event/<int:event_id>/', views.unfollow_event, name='unfollow_event')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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
    path('post/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('report/<int:report_id>/delete/', views.delete_reported_post, name='delete_reported_post'),
    path('report/<int:report_id>/ignore/', views.disregard_reported_post, name='disregard_reported_post'),
    path('toggle-like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('toggle-save/<int:post_id>/', views.toggle_save, name='toggle_save'),  
    path('add-comment/<int:post_id>/', views.comment_create, name='add_comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('saved_posts', views.saved_posts, name='saved_posts'),
    path('events', views.event_home, name='events'),
    path('announcements', views.announcement_home, name='announcements'),
    path('announcement_create', views.announcement_create, name='announcement_create'),
    path('announcements/<int:announcement_id>', views.announcement_detail, name='announcement_detail'),
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
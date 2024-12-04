from django.contrib import admin
from .models import Post, Comment, Like, Save, Report, Announcement, Event, Follow

# Customizing the Post admin interface
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'last_edited', 'is_deleted')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('is_deleted', 'date_posted')
    ordering = ('-date_posted',)
    date_hierarchy = 'date_posted'

# Customizing the Comment admin interface
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_posted', 'is_deleted')
    search_fields = ('content', 'author__username')
    list_filter = ('is_deleted', 'date_posted')

# Customizing the Like admin interface
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'liked_on')
    search_fields = ('author__username', 'post__title')
    list_filter = ('liked_on',)

# Customizing the Save admin interface
@admin.register(Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'saved_on')
    search_fields = ('author__username', 'post__title')

# Customizing the Report admin interface
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'reason_category', 'reported_on', 'is_resolved')
    search_fields = ('author__username', 'post__title', 'reason')
    list_filter = ('reason_category', 'is_resolved', 'reported_on')

# Customizing the Announcement admin interface
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_archived')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('is_archived', 'created_at')

# Customizing the Event admin interface
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location')
    search_fields = ('title', 'location', 'description')
    list_filter = ('start_date', 'end_date')

# # Customizing the Follow admin interface
# @admin.register(Follow)
# class FollowAdmin(admin.ModelAdmin):
#     list_display = ('user', 'event')
#     search_fields = ('user__username', 'event__title')

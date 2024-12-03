from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    liked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'post')

    def __str__(self):
        return f'{self.author} liked {self.post}'

class Save(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saves')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saves')
    saved_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'post')

    def __str__(self):
        return f'{self.author} saved {self.post}'

class Report(models.Model):
    HARASSMENT = 'HR'
    SPAM = 'SP'
    NUDITY = 'NU'
    VIOLENCE = 'VI'
    HATE_SPEECH = 'HS'
    OTHER = 'OT'

    REASON_CHOICES = [
        (HARASSMENT, 'Harassment'),
        (SPAM, 'Spam'),
        (NUDITY, 'Nudity'),
        (VIOLENCE, 'Violence'),
        (HATE_SPEECH, 'Hate Speech'),
        (OTHER, 'Other'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports')
    reason = models.TextField()
    reason_category = models.CharField(max_length=2, choices=REASON_CHOICES)
    reported_on = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} reported {self.post}'
    
# experimental for now
class Notification(models.Model):
    NEW_COMMENT = 'NC'
    NEW_LIKE = 'NL'
    NEW_REPORT = 'NR'
    NEW_NOTIF = 'NN' # for purpose of avoiding null default

    EVENT_MAP = [
        (NEW_COMMENT, 'New Comment'),
        (NEW_LIKE, 'New Like'),
        (NEW_REPORT, 'New Report'),
    ]
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=2, choices=EVENT_MAP, default=NEW_NOTIF)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.recipient} - {self.get_event_type_display()}'
    
    def get_url(self):
        if self.post:
            return reverse('post_detail', kwargs={'post_id': self.post.id})
        return '#'

    class Meta: 
        ordering = ['-created_at']

class Announcement(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title        
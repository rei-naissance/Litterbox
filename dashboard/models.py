from django.db import models
from django.conf import settings
from django.urls import reverse
from django.forms import ValidationError
from tinymce import models as tinymce_models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = tinymce_models.HTMLField()
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
        return f'{self.author} notified {self.post}'
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='')
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    user = models.ForeignKey(
        'authentication.Student', on_delete=models.CASCADE, 
        related_name="events", null=True, blank=True
    )
    
    organizer = models.ForeignKey(
        'authentication.Student', on_delete=models.CASCADE, 
        related_name="organized_events", null=True, blank=True
    )

    def clean(self):
        if self.user and self.organizer:
            raise ValidationError("You must specify either a user or an organizer, but not both.")
    
    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Follow(models.Model):
    user = models.ForeignKey('authentication.Student', related_name="followed_events", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="followers", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} follows event: {self.event.title}"

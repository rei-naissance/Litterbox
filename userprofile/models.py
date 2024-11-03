from django.db import models
from authentication.models import Student

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,related_name='profile', null=True)
    username = models.CharField(null=True,max_length=150)
    bio = models.TextField(null=True, blank=True)

    cover_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    title = models.CharField(null=True,max_length=150)  
    
    post_count = models.IntegerField(default=0)  
    comment_count = models.IntegerField(default=0)  
    event_count = models.IntegerField(default=0)  

    social_links = models.JSONField(null=True,default=dict, blank=True)  

    def save(self, *args, **kwargs):
        if not self.username and self.student:
            self.username = f"@{self.student.first_name}{self.student.last_name}"
        super().save(*args, **kwargs)

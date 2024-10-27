from django.db import models


class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)

    cover_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    title = models.CharField(null=True,max_length=255)  
    
    post_count = models.IntegerField(default=0)  
    comment_count = models.IntegerField(default=0)  
    event_count = models.IntegerField(default=0)  

    social_links = models.JSONField(null=True,default=dict, blank=True)  

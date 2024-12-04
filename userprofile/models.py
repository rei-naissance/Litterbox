from django.db import models

class Profile(models.Model):
    student = models.OneToOneField('authentication.Student', on_delete=models.CASCADE ,related_name='profile')
    username = models.CharField(null=True,max_length=150)
    bio = models.TextField(null=True, blank=True)

    cover_image = models.ImageField(null=True, blank=True, upload_to="images/",  default="images/cover_photo.png")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default_profile_pic.png")
    
    title = models.CharField(null=True, blank=True ,max_length=150)  
    
    post_count = models.IntegerField(default=0)  
    comment_count = models.IntegerField(default=0)  
    like_count = models.IntegerField(default=0)  

    social_links = models.JSONField(null=True,default=dict, blank=True)  

    def save(self, *args, **kwargs):
        if not self.username and self.student:
            self.username = f"@{self.student.first_name}{self.student.last_name}"
        super().save(*args, **kwargs)

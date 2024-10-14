from django.db import models

# Create your models here.
class profile(models.Model):
    bio = models.CharField('Bio', max_length=1000)
    cover_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
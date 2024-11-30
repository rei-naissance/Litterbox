from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from userprofile.models import Profile

@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_active:
        Profile.objects.create(student=instance)
    elif instance.is_active and not hasattr(instance, 'profile'):
        Profile.objects.create(student=instance)
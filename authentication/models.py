from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_email(email):
    if not email.endswith('@cit.edu'):
        raise ValidationError('Email must be a CIT-U email address.')

class StudentManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Student(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_bio = models.TextField(blank=True, default="This user has nothing to say")
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    # idelete guro nako ni
    def save(self, *args, **kwargs):
        match = re.match(r'^([a-zA-Z]+)\.([a-zA-Z]+)@cit\.edu$', self.email)
        if match:
            self.first_name = match.group(1).capitalize()
            self.last_name = match.group(2).capitalize()
        super(Student, self).save(*args, **kwargs)
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
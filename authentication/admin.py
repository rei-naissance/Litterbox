from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

class StudentAdmin(UserAdmin):
    # Specify the fields to display in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_verified')
    list_filter = ('is_active', 'is_admin', 'is_verified')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

# Register the Student model with the custom admin class
admin.site.register(Student, StudentAdmin)

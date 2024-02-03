from django.contrib import admin
from .models import *
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     # Customize the way the user model is displayed in the admin interface if needed
#     list_display = ('username', 'email', 'name', 'gender', 'phone', 'profile_picture', 'date_of_birth')

# # Register the custom user model with the admin site
# admin.site.register(CustomUser, CustomUserAdmin)

class PatientInline(admin.TabularInline):
    model = Patient
    extra = 1  # Number of empty forms to display for adding new patients
    
class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatientInline]

class PatientAdmin(admin.ModelAdmin):
    readonly_fields=('doctor')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Donor)
admin.site.register(Patient)

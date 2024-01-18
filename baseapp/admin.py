from django.contrib import admin
from .models import Donor,Patient,Doctor

# Register your models here.
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

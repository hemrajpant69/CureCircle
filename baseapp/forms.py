from django import forms
from .models import Patient, Doctor

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

class PatientAndDoctorForm(forms.ModelForm):
    class Meta:
            model = Patient
            fields = ['name', 'email', 'phone', 'age', 'gender', 'drecommend', 'wrecommend', 'fundamount', 'bloodgroup', 'healthissue', 'hospitalization_condition']

    # Additional fields from Doctor model
    doctor_name = forms.CharField(max_length=50, required=True)
    specialization = forms.CharField(max_length=50, required=True)

    def save(self, commit=True):
        # Save the Patient instance
        patient_instance = super(PatientAndDoctorForm, self).save(commit=False)
        # Check if doctor with the provided name exists, create if not
        doctor_name = self.cleaned_data['doctor_name']
        specialization = self.cleaned_data['specialization']
        doctor_instance, created = Doctor.objects.get_or_create(name=doctor_name, specialization=specialization)
        # Associate the doctor with the patient
        patient_instance.doctor = doctor_instance
        if commit:
            patient_instance.save()
        return patient_instance
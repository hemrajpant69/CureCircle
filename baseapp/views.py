from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from .forms import PatientAndDoctorForm


# Create your views here.
def home(request):
    if Patient.objects.exists():
        patients=Patient.objects.all()
    else:
        patients = None
    return render(request, 'baseapp/index.html', {'patients': patients})

def donate(request):
    return render(request, 'baseapp/donate.html')

def requestfund(request):
    doctors = Doctor.objects.all()
    return render(request, 'baseapp/requestfund.html', {
        "doctors": doctors
        })

def about(request):
    return render(request,'baseapp/about.html')

def requestlanding(request):
        if request.method=='POST':  
            p_name=request.POST.get('patientName')
            p_age=request.POST.get('age')
            p_gender=request.POST.get('gender')
            p_phone=request.POST.get('contactPatient')
            p_email=request.POST.get('emailPatient')
            p_bloodgroup=request.POST.get('bloodgroupPatient')
            p_healthissue=request.POST.get('healthissue')
            p_hospitalcondition=request.POST.get('hospitalCondition')
            p_fundamount=request.POST.get('fundAmount')
            p_picture = request.FILES.get('picture')
            p_drecommend=request.FILES.get('drecommend')
            p_wrecommend=request.FILES.get('wrecommend')

            d_name=request.POST.get('doctorName')
            d_hospitalname=request.POST.get('hospital')
            d_phone=request.POST.get('contactDoctor')
            d_email=request.POST.get('emailDoctor')
            d_specialization=request.POST.get('specialization')

            doctor, created=Doctor.objects.get_or_create(name=d_name, email= d_email, phone= d_phone, hospital= d_hospitalname, specialization= d_specialization)

            if created:
                 doctor.save()

            patient=Patient.objects.create(picture = p_picture, doctor=doctor, name= p_name, email= p_email, phone= p_phone, age= p_age, gender= p_gender, drecommend= p_drecommend, wrecommend= p_wrecommend, fundamount= p_fundamount, bloodgroup= p_bloodgroup, healthissue= p_healthissue, hospitalization_condition= p_hospitalcondition)

            patient.save()

            return redirect('requestlanding')
            # doctors=Doctor.objects.all()

            # doctor_info = [{'name': doctor.name, 'specialization': doctor.specialization} for doctor in doctors]

            # patients=Patient.objects.create(doctor=doctor_info, name=p_name, age=p_age, gender=p_gender, phone=p_phone, email=p_email, bloodgroup=p_bloodgroup,  healthissue=p_healthissue, hospitalization_condition=p_hospitalcondition, fundamount=p_fundamount, drecommend=p_drecommend, wrecommend=p_wrecommend)

            # patients.save()

            # views.py
             
        return render(request, 'baseapp/requestlanding.html')


def donatelanding(request):
    donordata={}
    if request.method=="POST":
         name=request.POST.get('donorName')
         email=request.POST.get('donorEmail')
         phone=request.POST.get('donorPhone')
         bloodgroup=request.POST.get('bloodgroupDonor')
         amount=request.POST.get('amount')

         donor, created=Donor.objects.get_or_create(name=name, amount=amount, email=email, phone=phone, bloodgroup=bloodgroup)
         if created:
            donor.save()

         return render(request,'baseapp/donatelanding.html', {'donordata': donor})
    return render(request, 'baseapp/donatelanding.html')

def contact(request):
    return render(request, 'baseapp/contact.html')
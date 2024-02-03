from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import PatientAndDoctorForm, SignupForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login_page')
def home(request):
    if Patient.objects.exists():
        patients=Patient.objects.all()
    else:
        patients = None
    
    context = {'patients': patients, 'title': 'Home | CureCircle'}
    return render(request, 'baseapp/index.html', context )

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login_page')
    else:
            form = SignupForm()
    
    context = {'title': 'Sign Up | CureCircle', 'form': form}
    return render(request, 'baseapp/signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=uname, password=pwd)
        if(user is not None):
            login(request, user)

            return redirect('home_page')
        
        else:
            return render(request, 'baseapp/login.html', {'error_message': 'Invalid login credentials'})
    context = {'title': 'Log in | CureCircle'}
    return render(request, 'baseapp/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
def donate(request):
    context = {'title': 'Donate fund | CureCircle'}
    return render(request, 'baseapp/donate.html', context)

@login_required(login_url='login_page')
def requestfund(request):
    doctors = Doctor.objects.all()
    group = Patient.GROUP
    context = {'title': 'Request for fund | CureCircle', "doctors": doctors, 'group':group}
    return render(request, 'baseapp/requestfund.html', context)


def about(request):
    context = {'title': 'About | CureCircle'}
    return render(request,'baseapp/about.html', context)

@login_required(login_url='login_page')
def requestlanding(request):
        if request.method=='POST':
            p_user = request.user
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
            # d_hospitalname=request.POST.get('hospital')
            # d_phone=request.POST.get('contactDoctor')
            # d_email=request.POST.get('emailDoctor')
            # d_specialization=request.POST.get('specialization')

            doctor = Doctor.objects.get(name=d_name)

            patient = Patient.objects.create(user= p_user ,picture = p_picture, doctor=doctor, name= p_name, email= p_email, phone= p_phone, age= p_age, gender= p_gender, drecommend= p_drecommend, wrecommend= p_wrecommend, fundamount= p_fundamount, bloodgroup= p_bloodgroup, healthissue= p_healthissue, hospitalization_condition= p_hospitalcondition)

            patient.save()

            return redirect('requestlanding')
            # doctors=Doctor.objects.all()

            # doctor_info = [{'name': doctor.name, 'specialization': doctor.specialization} for doctor in doctors]

            # patients=Patient.objects.create(doctor=doctor_info, name=p_name, age=p_age, gender=p_gender, phone=p_phone, email=p_email, bloodgroup=p_bloodgroup,  healthissue=p_healthissue, hospitalization_condition=p_hospitalcondition, fundamount=p_fundamount, drecommend=p_drecommend, wrecommend=p_wrecommend)

            # patients.save()

            # views.py
        context = {'title': 'Request received | CureCircle', "patient": patient}
             
        return render(request, 'baseapp/requestlanding.html', context)

@login_required(login_url='login_page')
def donatelanding(request):
    context = {}
    if request.method=="POST":
         name=request.POST.get('donorName')
         email=request.POST.get('donorEmail')
         phone=request.POST.get('donorPhone')
         bloodgroup=request.POST.get('bloodgroupDonor')
         amount=request.POST.get('amount')

         donor, created=Donor.objects.get_or_create(name=name, amount=amount, email=email, phone=phone, bloodgroup=bloodgroup)
         if created:
            donor.save()
         context = {'title': 'Fund received | CureCircle', 'donordata': donor}
         return render(request,'baseapp/donatelanding.html', context)
    return render(request, 'baseapp/donatelanding.html')


def contact(request):
    context = {'title': 'Contact | CureCircle'}
    return render(request, 'baseapp/contact.html', context)

@login_required(login_url='login_page')
def patientPage(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'title': patient.name, 'patient': patient}
    return render(request, 'baseapp/patient.html', context)
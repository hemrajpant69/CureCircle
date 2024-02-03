from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home_page'),
    path('login/', views.loginPage, name = 'login_page'),
    path('signup/', views.signup, name = 'signup_page'),
    path('logout/', views.logoutPage, name= 'logout_page'),
    path('donate/', views.donate, name = 'donation_page'),
    path('request-fund/', views.requestfund, name = 'request_page'),
    path('requestlanding/', views.requestlanding, name ='requestlanding'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
    path('donatelanding/', views.donatelanding, name= 'donatelanding_page'),
    path('donate/', views.donate, name = 'donate_page'),
    path('patient/<str:pk>/', views.patientPage, name= 'patient_page'),
]

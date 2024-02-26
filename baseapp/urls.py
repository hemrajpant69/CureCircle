from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home_page'),
    path('profile/<str:pk>/', views.profilePage, name= 'profile_page'),
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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='baseapp/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='baseapp/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='baseapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='baseapp/password_reset_complete.html'), name='password_reset_complete'),
]

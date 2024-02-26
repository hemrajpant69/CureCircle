from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     GENDER=(
#         ('Male','Male'),
#         ('Female', 'Female'),
#         ('Others', 'Others')
#     )

#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=50, null=True)
#     date_of_birth = models.DateField(auto_now_add=True, null=True)
#     profile_picture = models.ImageField(upload_to = 'profile/', null=True, default= 'profile/default.jpg')
#     phone = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
#     gender = models.CharField(max_length=20, null=True, choices=GENDER)

#     def __str__(self):
#         return self.username

# Create your models here.

# class BloodGroup(models.Model):
    # GROUP=(
    #     ('O positive','O positive'),
    #     ('O negative','O negative'),
    #     ('A positive','A positive'),
    #     ('A negative','A negative'),
    #     ('B positive','B positive'),
    #     ('B negative','B negative'),
    #     ('AB positive','AB positive'),
    #     ('AB negative','AB negative'),
    #     ("Don't know", "Don't know")
    # )

#     bloodgroup=models.CharField(max_length=15, choices=GROUP)

# class Profile(models.Model):
#     pass

class Donor(models.Model):
    GROUP=(
        ("Don't know", "Don't know"),
        ('O positive','O positive'),
        ('O negative','O negative'),
        ('A positive','A positive'),
        ('A negative','A negative'),
        ('B positive','B positive'),
        ('B negative','B negative'),
        ('AB positive','AB positive'),
        ('AB negative','AB negative')
    )
    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    bloodgroup=models.CharField(max_length=20, blank=False, default="Don't know", choices=GROUP)
    amount=models.PositiveBigIntegerField(default=0, null=True, blank=False)
    def __str__(self):
        return self.name



class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50, blank=False)
    phone=models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],blank=False)
    hospital=models.CharField(max_length=50,blank=False, null=True)
    specialization=models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    GROUP=(
        ("Don't know", "Don't know"),
        ('O positive','O positive'),
        ('O negative','O negative'),
        ('A positive','A positive'),
        ('A negative','A negative'),
        ('B positive','B positive'),
        ('B negative','B negative'),
        ('AB positive','AB positive'),
        ('AB negative','AB negative')
    )
    GENDER=(
        ('Male','Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    name=models.CharField(max_length=50, blank=False, default=None)
    email=models.EmailField(max_length=50, blank=False, default=None)
    phone = models.IntegerField(validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)], blank=False, default=None)
    age=models.PositiveIntegerField(blank=False, null=True, default=0)
    gender=models.CharField(max_length=6, choices=GENDER, blank=False, default=None)
    doctor=models.ForeignKey(Doctor, on_delete=models.PROTECT)
    picture=models.ImageField(upload_to = 'pictures', max_length = 75, blank = False, null= True)
    drecommend=models.ImageField(upload_to='drecommend' ,max_length=50, blank=False, null=True)
    wrecommend=models.ImageField(upload_to='wrecommend', max_length=50, blank=False, null=True)
    fundamount=models.PositiveIntegerField(blank=False, null=True)
    bloodgroup=models.CharField(max_length=20, blank=False, default="Don't know", choices=GROUP, null=True)
    healthissue=models.TextField(blank=False, default=None)
    hospitalization_condition=models.TextField(blank=False, default=None)
    # bloodgroup=models.CharField(max_length=20, choices=GROUP, unique=True)
    # bloodgroup=models.ForeignKey(BloodGroup, null=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import AbstractUser
from luminarapi.models import Course

from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):
    # Add your custom fields here
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    ADMIN = 'admin'
    FACULTY = 'faculty'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (FACULTY, 'Faculty'),
    ]

    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Student(BaseUser):
    full_name = models.CharField(max_length=50)
    selected_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent_no = models.CharField(max_length=13)
    phone = models.CharField(max_length=13)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class CustomAdmin(BaseUser):
    
    pass




class WaitingList(models.Model):
    student= models.OneToOneField(Student, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    selected_course = models.CharField(max_length=50)

    def __str__(self):
        return self.student.username

    def __str__(self):
        return self.username




class Batch(models.Model):
   
    batch_name = models.CharField(max_length=100)
    batch_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    coursename=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="crs")

    def __str__(self):
        return self.batch_name
    

class AddStudent(models.Model):
   
     stud = models.ForeignKey(Student, on_delete=models.CASCADE)
     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
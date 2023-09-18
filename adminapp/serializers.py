from rest_framework import serializers
from luminarapi.serializers import DetailsSerializer

from .models import CustomAdmin,Student,WaitingList,Batch,AddStudent
from luminarapi.models import Course


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = CustomAdmin
        fields = ["id", "username", "password", "email", "phone_number","designation","role"]

    def create(self, validated_data):
        return CustomAdmin.objects.create_user(**validated_data)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title"] 

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    
    class Meta:
        model = Student
        fields = ["id","username","password","gender","dob","phone","full_name","selected_course","email","parent_no"]
    
    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)

class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = '__all__'
        

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields="__all__"


class AddStudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = AddStudent
        fields = '__all__'
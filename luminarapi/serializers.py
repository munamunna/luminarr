from rest_framework import serializers

from luminarapi.models import DemoClass,Course,Batch,Overview,Attendance,Assignment,Announcement,LiveClass,VideoScreen,Test,JobPortal,VideoScreenClass,Logo,Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"

class DetailsSerializer(serializers.ModelSerializer):
    
    modules = ModuleSerializer(many=True,read_only=True)  # Include nested serialization of related modules

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'offline_fees', 'online_fees', 'thumbnail', 'full_name', 'cochin', 'calicut', 'modules']



class BatchSerializer(serializers.ModelSerializer):
     id=serializers.CharField(read_only=True)
     class Meta:
         model=Batch
         fields="__all__"
class OverviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    subjects = serializers.SerializerMethodField()
    class Meta:
         model=Overview
         fields="__all__"
    def get_subjects(self, obj):
        # Assuming subjects are stored as a comma-separated string in the database
        subjects_string = obj.subjects
        return [subject.strip() for subject in subjects_string.split(',')]
class AttendanceSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Attendance
        fields="__all__"
class AssignmentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Assignment
        fields="__all__"
class AnnouncementSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Announcement
        fields="__all__"

class VideoScreenSerializer(serializers.ModelSerializer):
    # id=serializers.CharField(read_only=True)
    course_title = serializers.CharField(source='select_course.title', read_only=True)
    batch_name=serializers.CharField(source='select_batch.batch_name',read_only=True)
    class Meta:
        model=VideoScreen
        fields="__all__"
class TestSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Test
        fields="__all__"
class JobPortalSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=JobPortal
        fields="__all__"

class VideoScreenClassSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='name.thumbnail', read_only=True) 
    class Meta:
        model = VideoScreenClass
        fields ='__all__'

class DemoSerializers(serializers.ModelSerializer):
    videos = VideoScreenClassSerializer(many=True, read_only=True)

    class Meta:
        model = DemoClass
        fields = ['id', 'title', 'thumbnail','videos']
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class LiveClassSerializer(serializers.ModelSerializer):
    logo=LogoSerializer()
    id=serializers.CharField(read_only=True)
    class Meta:
        model=LiveClass
        fields="__all__"







   



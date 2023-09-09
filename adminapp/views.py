from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomAdmin,Student,WaitingList,Batch,AddStudent
from adminapp.serializers import CustomUserSerializer,StudentSerializer,WaitingListSerializer,BatchSerializer,AddStudentSerializer
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser, IsStudentUser 

class CustomAdminView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomAdmin.objects.all()
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user object
        
        total_registered_users = CustomAdmin.objects.count()  # Calculate total registered users dynamically
        
        response_data = {
            "status": "ok",
            "data": [{
                "id": user.id,
                "username": user.username,
                "password":user.password,
                "email": user.email,
                "phone_number": user.phone_number,
                "designation": user.designation,
                "role": user.role,
            }],
            "totalResults": total_registered_users,
        }
        
        return Response(response_data)


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user object

        # Add student to waiting list with name and ID
        waiting_list_entry = WaitingList(
            student=user,
            username=user.username,
            phone=user.phone,
            selected_course=user.selected_course
        )
        waiting_list_entry.save()

        total_registered_users = Student.objects.count()  # Calculate total registered users dynamically
        
        response_data = {
            "status": "ok",
            "data": {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
                "dob": user.dob,
                "selected_course": user.selected_course,
                "parent_no": user.parent_no
            },
            "totalResults": total_registered_users,
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class WaitingListView(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = WaitingListSerializer
    queryset = WaitingList.objects.all()

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
class BatchView(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()

    # ... (other methods)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)

            response_data = {
                'status': 'ok',
                'data': {
                    'count': queryset.count(),
                    'results': serializer.data
                }
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # ... (other methods)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response_data = {
                'status': 'ok',
                'data': {
                    'count': Batch.objects.count(),
                    'results': BatchSerializer(Batch.objects.all(), many=True).data
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    # ... (other methods)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)

            response_data = {
                'status': 'ok',
                'data': serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    # ... (other methods)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                'status': 'ok',
                'data': {
                    'message': 'Batch updated successfully',
                    'batch': serializer.data
                }
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    # ... (other methods)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

            response_data = {
                'status': 'ok',
                'data': {
                    'message': 'Batch deleted successfully'
                }
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AddStudentToBatch(APIView):
    def post(self, request, batch_id):
        try:
            batch = Batch.objects.get(pk=batch_id)
        except Batch.DoesNotExist:
            return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AddStudentSerializer(data=request.data)
        
        if serializer.is_valid():
            student = serializer.validated_data['stud']

            # Create an AddStudent instance to associate the student with the batch
            add_student = AddStudent.objects.create(stud=student, batch=batch)
            
            # Remove student from waiting list
            try:
                waiting_list_entry = WaitingList.objects.get(student=student)
                waiting_list_entry.delete()
            except WaitingList.DoesNotExist:
                pass  # The student was not found in the waiting list
            
            return Response({'message': 'Student added to batch successfully', 'student_id': student.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddedView(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = AddStudentSerializer
    queryset = AddStudent.objects.all()
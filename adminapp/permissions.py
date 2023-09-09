from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user and request.user.role == 'admin'

class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a student
        return request.user and request.user.role == 'student'

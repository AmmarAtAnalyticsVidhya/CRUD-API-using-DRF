from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # Implement your custom permission logic here
        if request.method == 'GET':
            return True  # Allow read-only access for all users
        return False # Allow access for all users (for testing purposes)
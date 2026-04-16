from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
# permission_classes = [IsAdminUser] # Uncomment this line to restrict access to admin users only
# permission_classes = [IsAuthenticated]  # Uncomment this line to require authentication for all users
# permission_classes = [AllowAny]  # Uncomment this line to allow unrestricted access to all users
# permission_classes = [IsAuthenticatedOrReadOnly]  # Uncomment this line to allow read-only access for unauthenticated users and full access for authenticated users
# permission_classes = [DjangoModelPermissions]  # Uncomment this line to use Django's built-in model permissions for fine-grained access control
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Uncomment this line to use Django's built-in model permissions for fine-grained access control
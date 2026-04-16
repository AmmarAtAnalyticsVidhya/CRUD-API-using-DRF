from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
# permission_classes = [IsAuthenticated]  # Uncomment this line to require authentication for all users
# permission_classes = [AllowAny]  # Uncomment this line to allow unrestricted access to all users

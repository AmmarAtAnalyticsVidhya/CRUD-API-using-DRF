from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app import views
from .views import BookViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


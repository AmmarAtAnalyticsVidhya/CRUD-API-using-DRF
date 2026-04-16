from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
from .models import Book
from rest_framework import serializers
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_published_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
    
    def validate_title(self, value):
        if len(value) > 100 or len(value) < 2:
            raise serializers.ValidationError("Title must be between 2 and 100 characters.")
        return value
    
    def validate_author(self, value):
        if len(value) > 100 or len(value) < 2:
            raise serializers.ValidationError("Author name must be between 2 and 100 characters.")
        return value
    
    def validate(self, data):
        if 'title' in data and 'author' in data:
            if Book.objects.filter(title=data['title'], author=data['author']).exists():
                raise serializers.ValidationError("A book with this title and author already exists.")
        return data
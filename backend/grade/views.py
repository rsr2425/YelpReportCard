from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.

class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # queryset = Review.objects.all()
    
    def get_queryset(self):
        return Review.objects.grade_reviews(Review.objects.all())

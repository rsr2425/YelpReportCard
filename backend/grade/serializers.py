from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'review_text',
            'food_grade',
            'service_grade',
            'vibe_grade',
            )
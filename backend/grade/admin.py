from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'review_text',
        'food_grade',
        'service_grade',
        'vibe_grade',
        )

# Register your models here.

admin.site.register(Review, ReviewAdmin)
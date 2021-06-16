from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class LetterGrade(models.TextChoices):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    F = 'F'
    NR = 'NR', _('Not Rated')

class Review(models.Model):
    title = models.CharField(max_length=120)
    review_text = models.TextField()
    food_grade = models.CharField(
        max_length=2,
        choices=LetterGrade.choices,
        default=LetterGrade.NR
    )
    service_grade = models.CharField(
        max_length=2,
        choices=LetterGrade.choices,
        default=LetterGrade.NR
    )
    vibe_grade = models.CharField(
        max_length=2,
        choices=LetterGrade.choices,
        default=LetterGrade.NR
    )

    def _str_(self):
        return self.title
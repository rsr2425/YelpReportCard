from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _

from .grade_gen import grade, sample_set

# Create your models here.


class LetterGrade(models.TextChoices):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    F = 'F'
    NR = 'NR', _('Not Rated')


class ReviewManager(models.Manager):
    def grade_reviews(self, reviews_qset: QuerySet):
        for review_obj in reviews_qset:
            # TODO find out if this is necessary (i.e. is django smart enough
            #  to detect whether changes have been made to the object.)
            updated = False
            if review_obj.food_grade == LetterGrade.NR:
                review_obj.food_grade = grade(review_obj.review_text,
                                              sample_set, "food")
                updated = True
            if review_obj.service_grade == LetterGrade.NR:
                review_obj.service_grade = grade(review_obj.review_text,
                                              sample_set, "service")
                updated = True
            if review_obj.vibe_grade == LetterGrade.NR:
                review_obj.vibe_grade = grade(review_obj.review_text,
                                              sample_set, "vibe")
                updated = True
            if updated: review_obj.save()
        return reviews_qset


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

    objects = ReviewManager()

    def _str_(self):
        return self.title
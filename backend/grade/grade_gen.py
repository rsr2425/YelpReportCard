"""

A module for grading restuarant review text according to the categories outlined in
the list CATEGORIES. A pre-loaded pandas DataFrame is loaded up in order to provide
a baseline for scoring reviews and assigning a letter grade.

"""

from sklearn.metrics.pairwise import cosine_similarity as cosim
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from django.contrib.staticfiles.storage import staticfiles_storage
from pathlib import Path

import os
import spacy
import scipy.stats as stats
import pandas as pd

nlp = spacy.load('en_core_web_sm')

sample_size = 10**4
seed = 777

CATEGORIES = ["food", "service", "vibe"]

# stored in staticfiles
sample_set = pd.read_csv(Path(staticfiles_storage.path('grade')) / 'sample_set.csv')

def assignCategory(input_text: str) -> str:
    """
    Assigns provided text to a category.

    Args
    ~~~~~~~~~~
    input_text - string containing the entire content of the text for which
        you would like to assign a category.

    Returns
    ~~~~~~~~~~
    An element from CATEGORIES that most appropriately matches the provided
    content.
    """
    nlp = spacy.load('en_core_web_sm')
    max_cosim_index, max_cosim = -1, -1

    input_text_vector = nlp(input_text).vector
    for i, cat in enumerate(CATEGORIES):
        curr_cosim_val = cosim(input_text_vector.reshape(1, -1),
                                nlp(cat).vector.reshape(1, -1))
        if max_cosim < curr_cosim_val:
            max_cosim = curr_cosim_val
            max_cosim_index = i

    return CATEGORIES[max_cosim_index]

def score(input_text: str) -> float:
    """
    Provides a numeric score that measures the positivity in a review.

    Args
    ~~~~~~~~~~
    input_text - string containing the entire content of the text for which
        you would like to score.

    Returns
    ~~~~~~~~~~
    A decimal value from 0 to 1 representing the percentage of the text
    that was determined by the sentiment engine to be positive.
    """
    sid = SentimentIntensityAnalyzer()
    sentiment_dict = sid.polarity_scores(input_text)
    return sentiment_dict["pos"]

def grade(review_text: str, sample_set: pd.DataFrame, cat: str=None) -> str:
    """
    Assigns a letter grade to review.

    This grade is assigned by the percentile rank of the score assigned to the
    review relative to the sample_set provided (scores in the top 20% get an A, next 20% get
    a B, etc. until finally the bottom 20% get assigned an F).

    This grading is done for a particular category. If none is specified, then
    a category will be assigned to the review.

    Args
    ~~~~~~~~~~
    input_text - string containing the entire content of the text for which
        you would like to assign a category.

    Returns
    ~~~~~~~~~~
    An element from CATEGORIES that most appropriately matches the provided
    content.
    """
    if cat is None:
        cat = assignCategory(review_text)
    elif cat not in CATEGORIES:
        raise ValueError(f"Please specify a recognized category: {CATEGORIES}")
    x_food = score(review_text)
    sample_cat = sample_set[sample_set["category"] == cat]
    percentile_val = stats.percentileofscore(sample_cat.score, float(x_food))
    if percentile_val < 20:
        return "F"
    elif percentile_val < 40:
        return "D"
    elif percentile_val < 60:
        return "C"
    elif percentile_val < 80:
        return "B"
    else:
        return "A"
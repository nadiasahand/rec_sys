from django.urls import path

from recommender.views import *

urlpatterns = [
    path('movie-ranking/', MovieRanking.as_view(), name='movie_ranking'),
]

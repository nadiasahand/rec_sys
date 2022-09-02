import logging

import numpy as np

from recommender.apps import RecommenderConfig
from recommender.models import Movies


class RankingModule:
    logging.basicConfig(filename='./MyLog.log',
                        level=logging.INFO)

    def __init__(self, _uid, _movies):
        self.uid = _uid
        self.movies = _movies
        self.results = []

    def rank(self):
        logging.info("[INFO] starting to rank the movies")
        model = RecommenderConfig.model

        for index, movieId in enumerate(self.movies):
            movie = Movies.objects.get(pk=int(movieId))
            rating = model({
                "user_id": np.array([str(self.uid)]),
                "movie_title": np.array([movie.title])
            }).numpy()[0]
            logging.info("movie title and rating: %s,%s", movie.title, rating)
            dict = {
                "rank": index + 1,
                "movie": movie,
                "rating": rating
            }
            self.results.append(dict)

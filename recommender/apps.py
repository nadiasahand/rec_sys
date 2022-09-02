import tensorflow as tf
from django.apps import AppConfig

from movie_recommender import settings


class RecommenderConfig(AppConfig):
    model = tf.saved_model.load(settings.MODELS_DIR)
    name = 'recommender'

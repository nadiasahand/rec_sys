from rest_framework import serializers

from recommender.models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['_id', 'title', 'genres']


class RequestSerializer(serializers.Serializer):
    movie_ids = serializers.ListField(child=serializers.CharField())
    uid = serializers.IntegerField(default=0)

    class Meta:
        fields = ['uid', 'movie_ids']


class ResultSerializer(serializers.Serializer):
    movie = MovieSerializer(many=False)
    rank = serializers.IntegerField(default=0)
    rating = serializers.CharField(default='')

    class Meta:
        fields = ['movie', 'rank', 'rating']


class ResponseSerializer(serializers.Serializer):
    uid = serializers.IntegerField(default='')
    results = ResultSerializer(many=True)

    class Meta:
        fields = ['uid', 'results']

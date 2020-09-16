from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'imdb_score', 'genre', 'imdb_score', 'popularity')

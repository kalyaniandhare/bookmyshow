from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.filters import SearchFilter


class MovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'director', 'imdb_score')
    # permission_classes = [permissions.IsAuthenticated]
